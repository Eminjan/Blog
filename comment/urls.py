#!/usr/bin/python3
# -*-coding:utf-8 -*-
#Author:Eminjan
#@Time  :2018/4/13 9:25


from django.urls import path
from . import views

urlpatterns = [
    path('update_comment',views.update_comment,name="update_comment")
]