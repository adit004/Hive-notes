from tkinter.font import names

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from hivenotes_app import views, reader_views, manager_views, admin_views
from hivenotes_app.manager_views import accept_member

urlpatterns = [
    path('',views.home,name="home"),
    path('Login',views.Login,name="Login"),
    path('logout',views.logout_view,name="logout"),

    #reader
    path('reader_registor',reader_views.reader_registor,name="reader_registor"),
    path('reader_page',reader_views.reader_page,name="reader_page"),
    path('community_view',reader_views.community_view,name="community_view"),
    path('reader_profile',reader_views.reader_profile,name="reader_profile"),
    path('reader_update/<int:id>',reader_views.reader_update,name="reader_update"),
    path('join_request/<int:id>',reader_views.join_request,name="join_request"),
    path('joined_communities',reader_views.joined_communities,name="joined_communities"),
    path('article_post/<int:id>',reader_views.article_post,name="article_post"),
    path('article_detail/<int:id>',reader_views.article_detail,name="article_detail"),
    path('community_detail/<int:id>',reader_views.community_detail,name="community_detail"),
    path('download_pdf/<int:id>',reader_views.download_pdf_view,name="download_pdf"),

    # manager
    path('manager_page',manager_views.manager_page,name="manager_page"),
    path('manager_registor',manager_views.manager_registor,name="manager_registor"),
    path('create_community',manager_views.create_community,name="create_community"),
    path('members_manage',manager_views.members_manage,name="members_manage"),
    path('accept_member/<int:id>',manager_views.accept_member,name="accept_member"),
    path('deny_member/<int:id>',manager_views.deny_member,name="deny_member"),
    path('manager_profile',manager_views.manager_profile,name="manager_profile"),
    path('manager_update/<int:id>',manager_views.manager_update,name="manager_update"),

    #admin
    path('admin_page',admin_views.admin_page,name="admin_page"),
    path('manager_manage',admin_views.manager_manage,name="manager_manage"),
    path('accept_manager/<int:id>',admin_views.accept_manager,name="accept_manager"),
    path('deny_manager/<int:id>',admin_views.deny_manager,name="deny_manager"),
    path('article_view',admin_views.article_view,name="article_view")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
