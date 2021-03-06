from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=20)
    age = models.SmallIntegerField(verbose_name='年龄')
    SEX_CHOICES = (
        (0, '女'),
        (1, '男'),
    )
    sex = models.SmallIntegerField(verbose_name='性别',default=1,choices=SEX_CHOICES)

    qq = models.CharField(max_length=20,unique=True,error_messages={"unique":'qq号码重复!'})
    phone = models.CharField(verbose_name='电话',max_length=20,unique=True,error_messages={"unique":'电话号码重复!'})
    c_time = models.DateTimeField('创建时间',auto_now=True)
    e_time = models.DateTimeField('修改时间',auto_now=True)
    grade = models.ForeignKey('Grade',on_delete=models.SET_NULL,null=True)
    is_delete = models.BooleanField(default=False)#一般情况下我们不会直接删除数据，而是给数据加一个字段is_delete，来标记数据状态
    def __str__(self):
        return  "{}-{}".format(self.name,self.age)

class StudentDetail(models.Model):
    num = models.CharField('身份证',max_length=40,unique=True)
    college= models.CharField('毕业学校',max_length=20,default='')
    student = models.OneToOneField('Student',on_delete=models.CASCADE,related_name='detail')
    def __str__(self):
        return "{}".format(self.student.name)

class Grade(models.Model):
    name = models.CharField('班级名称',max_length=20)
    num = models.CharField('班期',max_length=20)

    def __str__(self):
        return "{}".format(self.name,self.num)

class Course(models.Model):
    name =models.CharField('课程名称',max_length=20)
    student = models.ManyToManyField('Student',through='Enroll')

    def __str__(self):
        return self.name

class Enroll(models.Model):
    student = models.ForeignKey('Student',on_delete=models.CASCADE)
    course = models.ForeignKey('Course',on_delete=models.CASCADE)
    pay = models.FloatField('缴费金额',default=0)
    c_time = models.DateTimeField('报名时间',auto_now_add=True)