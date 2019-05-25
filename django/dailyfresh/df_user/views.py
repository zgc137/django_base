#coding=utf-8
from _sha1 import sha1
from datetime import datetime
from django.http import JsonResponse
from .models import *
from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse
# from df_user.models import Student
# Create your views here.

def register(request):
    return render(request,'df_user/register.html')

def register_handle(request):

    #receive user input
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')

    #Judging 2 passwords
    if upwd != upwd2:
        return redirect('/user/register/')

    #encryption
    s1 = sha1()
    s1.update(upwd.encode("utf8"))
    upwd3 = s1.hexdigest()

   #create object
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()

    #register success redirect login.html
    return redirect('/user/login/')

def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

