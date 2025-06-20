from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from hivenotes_app.forms import LoginRegister, ReaderRegister


# Create your views here.
def home(request):
    return render(request,"home.html",)


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('/')
            elif user.is_reader:
                return redirect('reader_page')
            elif user.is_manager:
                return redirect('/')
        else:
            messages.info(request,"invalid username or password")
    return render(request,"signin.html")


def logout_view(request):
    logout(request)
    return redirect('home')