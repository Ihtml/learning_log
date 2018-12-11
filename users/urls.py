# _*_ coding: utf-8 _*_
__author__ = 'ife'
__date__ = '2018-12-11 23:52'

from django.urls import path
from django.contrib.auth.views import login

from . import views


app_name = 'learning_logs'
urlpatterns = [
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),
]