import io

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import get_template
from xhtml2pdf import pisa

from hivenotes_app.forms import LoginRegister, ReaderRegister, ArticleForm
from hivenotes_app.models import Members, Community, Reader, Articles


def reader_registor(request):
    login_form = LoginRegister()
    reader_form = ReaderRegister()

    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        reader_form = ReaderRegister(request.POST, request.FILES)
        if login_form.is_valid() and reader_form.is_valid():
            reader = login_form.save(commit=False)
            reader.is_reader = True
            reader.save()

            user1 = reader_form.save(commit=False)
            user1.user = reader
            user1.user.account_status = 'accepted'
            user1.save()
            return redirect('/')
    return render(request, "reader/registor.html", {'login_form': login_form, 'reader_form': reader_form})


@login_required(login_url='login')
def reader_page(request):
    articles = Articles.objects.all
    return render(request,"reader/home.html",{'articles':articles})


@login_required(login_url='login')
def reader_profile(request):
    reader = Reader.objects.get(user = request.user)
    return render(request,"reader/profile.html",{'user':reader})


@login_required(login_url='login')
def reader_update(request,id):
    data = Reader.objects.get(id=id)
    reader_form = ReaderRegister(instance=data)
    if request.method == 'POST':
        form1 = ReaderRegister(request.POST, instance=data)
        if form1.is_valid():
            form1.save()
            return redirect('reader_profile')
    return render(request,"reader/update.html",{'form':reader_form})


@login_required(login_url='login')
def community_view(request):
    reader = Reader.objects.get(user = request.user)
    members = Members.objects.filter(reader = reader)
    communities = Community.objects.all
    return render(request,"reader/community_view.html",{'communities':communities,'members':members})


@login_required(login_url='login')
def join_request(request,id):
    reader = Reader.objects.get(user = request.user)
    community = Community.objects.get(id = id)
    if Members.objects.filter(reader=reader,community=community).exists():
        messages.info(request, 'request pending ')
    else:
        member = Members()
        member.reader = reader
        member.community = community
        member.save()
    return redirect('community_view')


@login_required(login_url='login')
def joined_communities(request):
    reader_id = Reader.objects.get(user = request.user)
    member = Members.objects.filter(reader = reader_id, account_status = 'accepted')
    return render(request,"reader/joined_communities.html",{'member':member})


@login_required(login_url='login')
def article_post(request,id):
    member = Members.objects.get(id = id)
    article_form = ArticleForm()
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.member = member
            article.save()
            return redirect('reader_page')
    return render(request,"reader/article_post.html",{'form':article_form})


@login_required(login_url='login')
def article_detail(request, id):
    article = Articles.objects.get(id=id)
    return render(request, 'reader/article_detail.html', {'article': article})


@login_required(login_url='login')
def community_detail(request,id):
    reader_id = Reader.objects.get(user = request.user)
    community = Community.objects.get(id = id )
    articles = Articles.objects.filter(member__community=community)
    try:
        member = Members.objects.get(reader=reader_id,community=community)
    except:
        member = None
    context = {
        "community": community,
        "articles": articles,
        "member":member
    }
    return render(request,'reader/community_detail.html',context)


#pdf
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


@login_required(login_url='login')
def download_pdf_view(request,id):
    article  = Articles.objects.get(id = id)
    context = {
        "article":article
    }
    filename = f"{article.head}_file.pdf"
    pdf = render_to_pdf('reader/pdf_template.html', context)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response


