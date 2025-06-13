from django.urls import path

from hivenotes_app import views, reader_views

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.login,name="login"),
    #reader
    path('reader_registor',reader_views.reader_registor,name="reader_registor")
]