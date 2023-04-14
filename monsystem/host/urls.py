from django.urls import path, include,re_path
from . import  views
from .views import ListView #ListViewFull


urlpatterns = [
    path('', views.index, name='index'),
    path('disk/', views.disk, name='disk'),
    path('users/', views.users, name='users'),
    path('diff/', views.diff, name='diff'),
    path('monitor/', views.monitor, name='monitor'),
    path('about/', views.about, name='about'),
    path('auth/', views.auth, name='auth'),
    path('apidatas/', views.apidatas, name='apidatas'),

    re_path(r"^(?P<api_name>[a-z]+)", ListView, name='members-objects'),
   # re_path(r"^(?P<api_name>[a-z]+)", ListViewFull, name='allmembers-objects'),



]