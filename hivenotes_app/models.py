from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class LoginView(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_reader = models.BooleanField(default=False)


class Manager(models.Model):
    STATUS_CHOICES = {
        ('pending','pending'),
        ('accepted','accepted'),
        ('denied','denied'),
    }
    user = models.ForeignKey(LoginView,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    account_status= models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending',)



class Reader(models.Model):
    user = models.OneToOneField(LoginView,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)


class community(models.Model):
    reader = models.ForeignKey(Reader,on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE)

