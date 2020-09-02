from django.contrib import admin
from django.urls import path 
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    path('register',views.register , name="register"),
    path('login',views.login , name='login'),
    path('logout',views.logout , name='logout'),
    
  ]
