# _*_ coding: utf-8 _*_
__author__ = 'ife'
__date__ = '2018-12-11 23:52'

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'users'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),  name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]