from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class LoginView(AbstractUser):

    STATUS_CHOICES = {
        ('pending','pending'),
        ('accepted','accepted'),
        ('denied','denied'),
    }
    is_manager = models.BooleanField(default=False)
    is_reader = models.BooleanField(default=False)
    account_status= models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending',)



class Manager(models.Model):
    user = models.ForeignKey(LoginView,on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='profile/')
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)



class Reader(models.Model):
    user = models.OneToOneField(LoginView,on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='profile/')
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)


class Community(models.Model):
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='communityProfile/')
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 100)


class Members(models.Model):
    STATUS_CHOICES = {
        ('pending', 'pending'),
        ('accepted', 'accepted'),
        ('denied', 'denied'),
    }
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    community = models.ForeignKey(Community,on_delete=models.CASCADE)
    account_status= models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending',)



class Articles(models.Model):
    STATUS_CHOICES = {
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('denied', 'denied'),
    }
    member = models.ForeignKey(Members,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='articleImages/')
    head = models.CharField(max_length=20)
    subject = models.CharField(max_length=30)
    content = models.CharField(max_length=5000)
    date = models.DateField(auto_now_add=True)
    account_status= models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending',)


