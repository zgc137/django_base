#coding=utf-8
from _sha1 import sha1
from datetime import datetime
from django.http import JsonResponse
from .models import *
from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse
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

def detail(request,year,month,day,id):
    return HttpResponse("{}年{}月{}日学生ID为{}的详情".format(year,month,day,id))

def test1(request):
    return redirect(reverse('df_user:test'))

def test(request):
    return HttpResponse("<p>《霏霏》<br>云湿丝柳忆廉颇，<br>笑电霜滑自有天。<br>半雨江上怜锦碎，<br>梁尘落屑正乏贤。<br><p>")

def index(request):
    now = datetime.now()
    now1 = now.strftime('%Y{y}%m{m}%d{d}').format(y='年',m='月',d='日')
    L = [6,5,4]
    D = {'name':"菲菲",'age':18,'height':150}
    num = '8'
    sts = [
        {'name':'alex','age':18,'sex': 1},
        {'name':'菲菲','age':12,'sex': 0},
        {'name':'jack','age':28,'sex': 1},
    ]
    def func():
        return '菜徐坤'
    return render(request,'df_user/index.html',context={
        'now':now,
        'now1':now1,
        'L':L,
        'D':D,
        'func':func,
        'num':num,
        'sts':sts,
    })

def login01(request):
    return render(request,'df_user/login01.html')

def details(request,name):
    return HttpResponse('This is student {} detail page'.format(name))