from django.urls import path

from hivenotes_app import views, reader_views, manager_views

urlpatterns = [
    path('',views.home,name="home"),
    path('Login',views.Login,name="Login"),
    path('logout',views.logout_view,name="logout"),

    #reader
    path('reader_registor',reader_views.reader_registor,name="reader_registor"),
    path('reader_page',reader_views.reader_page,name="reader_page"),

    # manager
    path('manager_registor',manager_views.manager_registor,name="manager_registor"),
]