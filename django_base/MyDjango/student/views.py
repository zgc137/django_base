from django.core.paginator import Paginator
from django.shortcuts import render,reverse,redirect
from student.models import Student,Grade,StudentDetail
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.
def index(request):
    section = '学生列表'

    search = request.POST.get('search',' ').strip()
    if search:
        if search.isdigit():
            sts = Student.objects.filter(Q(qq=search)| Q(phone=search),is_delete=False)
        else:
            sts = Student.objects.filter(name=search,is_delete=False)
    else:
        sts = Student.objects.filter(is_delete=False)
    sts = sts.order_by('-c_time')#排序

    total_num = sts.count()#data total
    per_page = request.GET.get('per_page',5)
    page = request.GET.get('page',1)#current page

    p = Paginator(sts,per_page,allow_empty_first_page=True)
    sts = p.get_page(page)
    total_page = p.num_pages

    return render(request, 'student/index.html',context={
        'section':section,
        'sts':sts,
        'search':search,
        'total_num':total_num,
        'total_page':total_page,
        'page':page,
        'per_page':per_page,
    })

def student_delete(request,pk):
    student = Student.objects.get(pk=pk)
    student.is_delete = True
    student.save()
    return redirect(reverse('student:index'))

def student_detail(request,pk):
    section = '学生详情'
    grades = Grade.objects.all()
    student = Student.objects.get(pk=pk)
    studentDetail = StudentDetail.objects.get()
    return render(request,"student/student_detail.html",context={
        "section":section,
        "grades":grades,
        "student":student,
        "studentDetail":studentDetail,
    })

def student_add(request):
    section = '添加学生信息'
    grades = Grade.objects.all()
    if request.method == 'GET':
        return  render(request,'student/student_detail.html',context={
            'section':section,
            "grades": grades,
        })
    if request.method == 'POST':
        #获取提交的所有信息
        # name = request.POST.get('name')
        data = {
            'name':request.POST.get('name'),
            'age':request.POST.get('age'),
            'sex':request.POST.get('sex'),
            'qq':request.POST.get('qq'),
            'phone':request.POST.get('phone'),
        }
        student = Student.objects.create(**data)
        StudentDetail.objects.create(
            num=request.POST.get('num'),
            college=request.POST.get('college'),
            student=student #表关联
        )
        return  redirect(reverse('student:index'))

def student_edit(request,pk):
    section = '修改学生信息'
    student = Student.objects.get(pk=pk)
    student_Detail = StudentDetail.objects.all()

    if request.method == 'GET':
        return  render(request,'student/student_detail.html',context={
            'section': section,
            "student": student,
            'student_Detail':student_Detail,
        })
    if request.method == 'POST':
        grade_id = request.POST.get('grade')
        try:
            grade = Grade.objects.get(pk=grade_id)
        except:
            grade=None
            #学生信息
        student = Student.objects.get(pk=pk)
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.sex = request.POST.get('sex')
        student.qq = request.POST.get('qq')
        student.phone = request.POST.get('phone')
        student.grade = grade#表关联

        #学生详情
        try:
            detail = student.detail#表关系
        except:
            detail = StudentDetail()
            detail.student = student#表关联
        detail.num = request.POST.get('num')
        detail.college = request.POST.get('college')

        detail.save()
        student.save()

        return redirect(reverse('student:index'))

