from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from hivenotes_app.models import Manager, LoginView, Articles


@login_required(login_url='login')
def admin_page(request):
    return render(request,"admin/home.html")


@login_required(login_url='login')
def manager_manage(request):
    managers = Manager.objects.all
    return render(request,"admin/manager_view.html",{'managers':managers})


@login_required(login_url='login')
def accept_manager(request,id):
    manager_id = Manager.objects.get(id = id)
    user_id = manager_id.user.id
    manager = LoginView.objects.get(id = user_id )
    manager.account_status = 'accepted'
    manager.save()
    return redirect('manager_manage')


@login_required(login_url='login')
def deny_manager(request,id):
    manager_id = Manager.objects.get(id = id)
    user_id = manager_id.user.id
    manager = LoginView.objects.get(id= user_id)
    manager.account_status = 'denied'
    manager.save()
    return redirect('manager_manage')


@login_required(login_url='login')
def article_view(request):
    articles = Articles.objects.all().order_by('-date')
    return render(request, "admin/article_view.html", {'articles': articles})