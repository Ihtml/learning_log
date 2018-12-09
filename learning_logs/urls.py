# _*_ coding: utf-8 _*_
__author__ = 'ife'
__date__ = '2018-12-09 23:15'

from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index')
]