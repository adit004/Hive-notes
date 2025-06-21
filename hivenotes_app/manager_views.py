from django.shortcuts import redirect, render

from hivenotes_app.forms import ManagerRegister, LoginRegister


def manager_registor(request):
    login_form = LoginRegister()
    manager_form = ManagerRegister()

    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        manager_form = ManagerRegister(request.POST)
        if login_form.is_valid() and manager_form.is_valid():
            manager = login_form.save(commit=False)
            manager.is_manager = True
            manager.save()

            user1 = manager_form.save(commit=False)
            user1.user = manager
            user1.save()
            return redirect('/')
    return render(request, "manager/registor.html", {'login_form': login_form, 'manager_form': manager_form})


def manager_page(request):
    return render(request,"manager/home.html")