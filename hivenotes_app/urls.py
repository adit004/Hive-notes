from django.urls import path

from hivenotes_app import views, reader_views, manager_views, admin_views

urlpatterns = [
    path('',views.home,name="home"),
    path('Login',views.Login,name="Login"),
    path('logout',views.logout_view,name="logout"),

    #reader
    path('reader_registor',reader_views.reader_registor,name="reader_registor"),
    path('reader_page',reader_views.reader_page,name="reader_page"),

    # manager
    path('manager_page',manager_views.manager_page,name="manager_page"),
    path('manager_registor',manager_views.manager_registor,name="manager_registor"),

    #admin
    path('admin_page',admin_views.admin_page,name="admin_page"),
    path('manager_manage',admin_views.manager_manage,name="manager_manage"),
    path('accept_manager/<int:id>',admin_views.accept_manager,name="accept_manager"),
    path('deny_manager/<int:id>',admin_views.deny_manager,name="deny_manager"),
]