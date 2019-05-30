#!/usr/bin/env python
# encoding: utf-8
#@author: jack
#@contact: 935650354@qq.com
#@site: https://www.cnblogs.com/jackzz
#@software: PyCharm
#@time: 2019/5/30 14:55

from django import forms
from student.models import Student, StudentDetail


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['is_delete']#排除前台不需要的字段
        widgets = {
            'sex':forms.RadioSelect()
        }

class StudentDetailForm(forms.ModelForm):
    class Meta:
        model = StudentDetail
        exclude = ['student']

    def clean_num(self):
        data = self.cleaned_data.get('num')
        if not data[:-1].isdigit():
            self.add_error('num','你输入的身份证号码错误')



