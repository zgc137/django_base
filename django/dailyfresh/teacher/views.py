#coding=utf-8
from _sha1 import sha1
from datetime import datetime
from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse

# Create your views here.



def detail(request,year,month,day,id):
    return HttpResponse("{}年{}月{}日学生ID为{}的详情".format(year,month,day,id))

def test1(request):
    return redirect(reverse('df_user:test'))

def test(request):
    return HttpResponse("<p>《霏霏》<br>云湿丝柳忆廉颇，<br>笑电霜滑自有天。<br>半雨江上怜锦碎，<br>梁尘落屑正乏贤。<br><p>")

def index(request):
    now = datetime.now()
    format_str ='%Y-%m-%d %H:%M:%S'
    now1 = now.strftime(format_str)
    # now1 = now.strftime(format_str).format(y='年',m='月',d='日')
    now = now.strftime(format_str)
    L = [6,5,4]
    D = {'name':"菲菲",'age':18,'height':150}
    num = '8'
    # sts = Student.objects.all()
    sts = [
        {'name':'alex','age':18,'sex': 1,'course': ['Python','c']},
        {'name':'菲菲','age':12,'sex': 0,'course': ['Python','java']},
        {'name':'jack','age':28,'sex': 1,'course': ['Python','撩妹']}
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
        'format_str':format_str,
    })

def login01(request):
    return render(request,'df_user/login01.html')

def details(request,name):
    return HttpResponse('This is student {} detail page'.format(name))