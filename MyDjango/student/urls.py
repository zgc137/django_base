#!/usr/bin/env python
# encoding: utf-8
#@author: jack
#@contact: 935650354@qq.com
#@site: https://www.cnblogs.com/jackzz
#@software: PyCharm
#@time: 2019/5/24 0024 下午 21:07

from django.conf.urls import url
from django.urls import path
from . import views

app_name ='student'
urlpatterns =[
    path(r'index/',views.index,name="index"),
    path(r'student_delete/<pk>',views.student_delete,name="delete"),
    path(r'student_detail/<pk>',views.student_detail,name='detail'),
    path(r'student_edit/<pk>',views.student_edit,name='edit'),
    path(r'student_edit_form/<pk>',views.student_edit_form,name='edit_form'),
    path(r'student_add/',views.student_add,name='add'),
]
