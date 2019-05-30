#coding=utf-8
import os
from datetime import datetime
from .models import *
from django.shortcuts import render, redirect,reverse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from MyDjango.settings import MEDIA_ROOT
from  teacher.form import RegisterForm
# Create your views here.
def detail(request,year,month,day,id):
    return HttpResponse("{}年{}月{}日学生ID为{}的详情".format(year,month,day,id))

def test1(request):
    return redirect(reverse('teacher:test'))

def test(request):

    return HttpResponse("<p>《霏霏》<br>云湿丝柳忆廉颇，<br>笑电霜滑自有天。<br>半雨江上怜锦碎，<br>梁尘落屑正乏贤。<br><p>")

# def index(request):
#     num = request.COOKIES.get('num')
#     if num:
#         num = int(num) + 1
#     else:
#         num = 1
#     response = render(request, 'teacher/index.html', context={'num':num})
#     response.set_cookie('num',num,max_age=5) #max_age 整数值，单位为秒
#     return  response
    # now = datetime.now()
    # format_str ='%Y-%m-%d %H:%M:%S'
    # now1 = now.strftime(format_str)
    # # now1 = now.strftime(format_str).format(y='年',m='月',d='日')
    # now = now.strftime(format_str)
    # L = [6,5,4]
    # D = {'name':"菲菲",'age':18,'height':150}
    # num = '8'
    # # sts = Student.objects.all()
    # sts = [
    #     {'name':'alex','age':18,'sex': 1,'course': ['Python','c']},
    #     {'name':'菲菲','age':12,'sex': 0,'course': ['Python','java']},
    #     {'name':'jack','age':28,'sex': 1,'course': ['Python','撩妹']}
    # ]
    # def func():
    #     return '菜徐坤'
    # return render(request,'index.html',context={
    #     'now':now,
    #     'now1':now1,
    #     'L':L,
    #     'D':D,
    #     'func':func,
    #     'num':num,
    #     'sts':sts,
    #     'format_str':format_str,
    # })

def login01(request):

    return render(request, 'teacher/login01.html')

def index(request):
    name = request.session.get('name','游客')
    return  render(request,'teacher/new_index.html',context={'name':name})

def login(request):

    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST.get('pwd')
        if username == 'jack' and password =='123':
            request.session['name'] = username
            request.session.set_expiry(10)
            return redirect(reverse('teacher:index'))

    return  render(request, 'teacher/login.html')

def logout(request):
    request.session.flush()
    return  redirect(reverse('teacher:index'))

def details(request,name):
    return HttpResponse('This is student {} detail page'.format(name))

def upload(request):
    if request.method =='POST':
        # file = request.FILES.get('file')#upload a  file
        files = request.FILES.getlist('file')  #upload a many file
    #create file
        day_dir_name =datetime.now().strftime('%Y%m%d')
        day_dir = os.path.join(MEDIA_ROOT,day_dir_name)
        if not os.path.exists(day_dir):
            os.mkdir(day_dir)
        #save file
        for file in files:
            file_url = os.path.join(day_dir,file.name)
            with open(file_url,'wb') as fb:
                for line in file.chunks():
                    fb.write(line)

    return  render(request, 'teacher/upload.html')

def test2(request):
    sex = request.GET.get('sex')
    sex = int(sex)
    res = Student.objects.values('name','age','sex').filter(sex=sex)
    res = list(res)
    data = {'result':res}
    return JsonResponse(data)

def register(request):
    if request.method =='GET':
        form =RegisterForm()
        return render(request,'teacher/register.html',context={
            'form':form,
        })
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            email = form.cleaned_data.get('email')
            if password == password_repeat:
                return HttpResponse("注册成功")

        return render(request, 'teacher/register.html', context={
            'form': form,
        })
