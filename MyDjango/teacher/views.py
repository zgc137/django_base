#coding=utf-8
import os
from datetime import datetime
from .models import *
from django.shortcuts import render, redirect,reverse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from MyDjango.settings import MEDIA_ROOT
from  teacher.form import RegisterForm
from django.contrib.auth import authenticate,login,logout
from  django.contrib.auth.decorators import login_required,permission_required
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

def login_view(request):
    next_url = request.GET.get('next')
    # user = request.user #已登陆显示登陆用户，否则显示游客
    #判断是否登陆
    if request.user.is_authenticated:#匿名用户返回false
        if next_url:
            return redirect(next_url)
        return redirect(reverse('teacher:index'))
    # return render(request, 'teacher/login01.html')

    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST.get('pwd')
        user = authenticate(username=username,password=password)
        if user is not None:
            #登陆，将用户信息保存到session中
            login(request,user)
            if next_url:
                return redirect(next_url)
            return redirect(reverse('teacher:index'))
    return render(request,'teacher/login.html')

def index(request):
    name = request.session.get('name','游客')
    return  render(request,'teacher/new_index.html',context={'name':name})

# def login02(request):
#
#     if request.method == 'POST':
#         username = request.POST['user']
#         password = request.POST.get('pwd')
#         if username == 'jack' and password =='123':
#             request.session['name'] = username
#             request.session.set_expiry(10)
#             return redirect(reverse('teacher:index'))
#
#     return  render(request, 'teacher/login.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('teacher:index'))

# def logout01(request):
#     request.session.flush()
#     return  redirect(reverse('teacher:index'))



def details(request,name):
    return HttpResponse('This is student {} detail page'.format(name))

@permission_required('teacher.view_student',raise_exception=True)
@login_required  #默认未登录时跳转到accoounts/login
def upload(request):
    # if not request.user.is_authenticated:#未登录用户验证 限制登陆
    #     return redirect(reverse('teacher:login')+'?next={}'.format(request.path_info))#把当前路径做参数传递

    # if request.user.has_perm('teacher.view_student'):
    #     return HttpResponse('无权限查看')

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
