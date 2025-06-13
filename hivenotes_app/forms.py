from django import forms
from django.contrib.auth.forms import UserCreationForm

from hivenotes_app.models import LoginView, Reader, Manager


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = LoginView
        fields = ('username', 'password1', 'password2')


class ManagerRegister(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ('name', 'email', 'phone', 'address')


class ReaderRegister(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ('name', 'email', 'phone', 'address')

