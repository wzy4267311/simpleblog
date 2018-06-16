#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author : Wei Ziyu
# File: urls.py
from django.conf.urls import patterns,include,url
from . import views

urlpatterns=patterns('',
    url(r'^$',views.post_list),
)
