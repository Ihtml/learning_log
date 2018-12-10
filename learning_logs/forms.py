# _*_ coding: utf-8 _*_
__author__ = 'ife'
__date__ = '2018-12-10 22:42'

from django import forms

from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
