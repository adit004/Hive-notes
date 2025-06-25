from django.shortcuts import render, redirect

from hivenotes_app.models import Manager, LoginView


def admin_page(request):
    return render(request,"admin/home.html")


def manager_manage(request):
    managers = Manager.objects.all
    return render(request,"admin/manager_view.html",{'managers':managers})

def accept_manager(request,id):
    manager_id = Manager.objects.get(id = id)
    user_id = manager_id.user.id
    manager = LoginView.objects.get(id = user_id )
    manager.account_status = 'accepted'
    manager.save()
    return redirect('manager_manage')


def deny_manager(request,id):
    manager_id = Manager.objects.get(id = id)
    user_id = manager_id.user.id
    manager = LoginView.objects.get(id= user_id)
    manager.account_status = 'denied'
    manager.save()
    return redirect('manager_manage')
