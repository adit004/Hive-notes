from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class LoginView(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_reader = models.BooleanField(default=False)


class Manager(models.Model):
    user = models.ForeignKey(LoginView,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)


class Reader(models.Model):
    user = models.OneToOneField(LoginView,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    