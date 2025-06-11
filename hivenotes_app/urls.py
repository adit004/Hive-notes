from django.urls import path

from hivenotes_app import views

urlpatterns = [
    path('',views.home,name="home"),
]