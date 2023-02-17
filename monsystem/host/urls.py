from django.urls import path, include
from . import  views
urlpatterns = [
    path('', views.index, name='index'),
    path('disk/', views.disk, name='disk'),

    path('users/', views.users, name='users'),
    path('diff/', views.diff, name='diff'),
    path('monitor/', views.monitor, name='monitor'),
    path('about/', views.about, name='about'),
    path('auth/', views.auth, name='auth'),



]