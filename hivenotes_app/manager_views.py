from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from hivenotes_app.admin_views import manager_manage
from hivenotes_app.forms import ManagerRegister, LoginRegister, CommunityForm
from hivenotes_app.models import Manager, Community, Members, Articles


def manager_registor(request):
    login_form = LoginRegister()
    manager_form = ManagerRegister()

    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        manager_form = ManagerRegister(request.POST, request.FILES)
        if login_form.is_valid() and manager_form.is_valid():
            manager = login_form.save(commit=False)
            manager.is_manager = True
            manager.save()

            user1 = manager_form.save(commit=False)
            user1.user = manager
            user1.save()
            return redirect('/')
    return render(request, "manager/registor.html", {'login_form': login_form, 'manager_form': manager_form})

@login_required(login_url='login')
def manager_page(request):
    user_id = Manager.objects.get(user = request.user)
    try:
        community = Community.objects.get(manager = user_id)
        members = Members.objects.filter(community= community,account_status = "accepted")
        articles = Articles.objects.filter(member__community = community)
        context = {
            "community": community,
            "members" :members,
            "articles":articles
        }
        return render(request,"manager/home.html",context)
    except Community.DoesNotExist:
        return render(request, "manager/no_community.html")


@login_required(login_url='login')
def manager_profile(request):
    manager = Manager.objects.get(user = request.user)
    return render(request,"manager/profile.html",{'user':manager})


@login_required(login_url='login')
def manager_update(request,id):
    data = Manager.objects.get(id=id)
    manager_form = ManagerRegister(instance=data)
    if request.method == 'POST':
        form1 = ManagerRegister(request.POST, instance=data)
        if form1.is_valid():
            form1.save()
            return redirect('manager_profile')
    return render(request,"manager/update.html",{'form':manager_form})


@login_required(login_url='login')
def create_community(request):
    user = request.user
    manager_id = Manager.objects.get(user=user)
    community_form =CommunityForm()
    if request.method == 'POST':
        community_form = CommunityForm(request.POST, request.FILES)
        if community_form.is_valid():
            group = community_form.save(commit=False)
            group.manager = manager_id
            group.save()
        return redirect('manager_page')
    return render(request,"manager/create_community.html",{"form":community_form})

@login_required(login_url='login')
def members_manage(request):
    manager = Manager.objects.get( user = request.user )
    community_id = Community.objects.get( manager = manager)
    members = Members.objects.filter(community = community_id )
    return render(request,"manager/members_manage.html",{"members":members})


@login_required(login_url='login')
def accept_member(request,id):
    members = Members.objects.get(id = id )
    members.account_status = 'accepted'
    members.save()
    return redirect('members_manage')


@login_required(login_url='login')
def deny_member(request,id):
    members = Members.objects.get(id = id )
    members.account_status = 'denied'
    members.save()
    return redirect('members_manage')


