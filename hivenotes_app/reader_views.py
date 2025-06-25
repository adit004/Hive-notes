from django.shortcuts import redirect, render

from hivenotes_app.forms import LoginRegister, ReaderRegister
from hivenotes_app.models import Members, Community, Reader


def reader_registor(request):
    login_form = LoginRegister()
    reader_form = ReaderRegister()

    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        reader_form = ReaderRegister(request.POST)
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


def reader_page(request):
    return render(request,"reader/home.html",)


def reader_profile(request):
    reader = Reader.objects.get(user = request.user)
    return render(request,"reader/profile.html",{'user':reader})


def reader_update(request,id):
    data = Reader.objects.get(id=id)
    reader_form = ReaderRegister(instance=data)
    if request.method == 'POST':
        form1 = ReaderRegister(request.POST, instance=data)
        if form1.is_valid():
            form1.save()
            return redirect('reader_profile')
    return render(request,"reader/update.html",{'form':reader_form})



def community_view(request):
    communities = Community.objects.all
    return render(request,"reader/community_view.html",{'communities':communities})


def join_request(request,id):
    reader = Reader.objects.get(user = request.user)
    community = Community.objects.get(id = id)
    member = Members()
    member.reader = reader
    member.community = community
    member.save()
    return redirect('community_view')
