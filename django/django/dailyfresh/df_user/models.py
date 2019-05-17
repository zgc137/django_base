#coding=utf-8

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=20)
    ushou = models.CharField(max_length=20,default='')
    uaddress = models.CharField(max_length=100,default='')
    uyoubian = models.CharField(max_length=6,default='')
    uphone = models.CharField(max_length=11,default='')

    #default，blank是python层面的约束，不影响数据表结构，不需要进行数据迁移

class Student(models.Model):
    c_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField(null=True)
    sex = models.SmallIntegerField(default=1)
    qq = models.CharField(max_length=20,null=True)
    phone = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name