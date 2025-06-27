from django import forms
from django.contrib.auth.forms import UserCreationForm

from hivenotes_app.models import LoginView, Reader, Manager, Community, Articles


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
        fields = ('name', 'profile' , 'email', 'phone', 'address')


class ReaderRegister(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ('name', 'profile' ,'email', 'phone', 'address')


class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ('name','description','photo')



class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 50, 'class': 'my-textarea-class', }))

    class Meta:
        model = Articles
        fields = ('head','subject','content','photo')