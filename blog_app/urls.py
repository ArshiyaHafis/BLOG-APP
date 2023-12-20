from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name="main"),
    path('project/', views.get_project, name='project'),
    path('add_project/', views.post_project, name='add_project'),
    path('regsiter/', views.register, name='register'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('update_project/<str:name>/<int:id>',
         views.update_project, name='update_project'),
    path('delete_project/<str:name>/<int:id>',
         views.delete_project, name='delete_project'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('blogpost/<str:title>/<int:id>',
         views.blogpost, name='blogpost'),
    path('del_blog/<str:title>/<int:id>',
         views.del_blog, name='del_blog'),
    path('upd_blog/<str:title>/<int:id>',
         views.upd_blog, name='upd_blog'),
]
