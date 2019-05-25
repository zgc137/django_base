from django.db import models

# Create your models here.
from django.db.models import*


class Student(models.Model):

    name = models.CharField(max_length=20)
    age = models.SmallIntegerField(null=True)
    sex = models.SmallIntegerField(default=1)
    qq = models.CharField(max_length=20,null=True)
    phone = models.CharField(max_length=20,null=True)
    c_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    grade = models.ForeignKey('Grade',on_delete=models.SET_NULL,null=True,related_name='student')
    def __str__(self):
        return self.name

class StudentDetail(models.Model):
    college = models.CharField(max_length=20,default="")
    student = models.OneToOneField('Student',on_delete=CASCADE)


class Grade(models.Model):
    name = models.CharField('班级名称',max_length=20)
    num = models.CharField('班期',max_length=20)

    def __str__(self):
        return  "{}-{}".format(self.name,self.num)

class Course(models.Model):
    name = models.CharField('课程名称',max_length=20)
    student = models.ManyToManyField('Student',through='Enroll')

class Enroll(models.Model):
    student = models.ForeignKey('Student',on_delete=CASCADE)
    course = models.ForeignKey('Course',on_delete=CASCADE)
    c_time = models.DateTimeField('报名时间',auto_now_add=True)
    pay = models.FloatField('缴费金额',default=0)
