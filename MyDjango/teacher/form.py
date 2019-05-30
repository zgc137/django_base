#!/usr/bin/env python
# encoding: utf-8
#@author: jack
#@contact: 935650354@qq.com
#@site: https://www.cnblogs.com/jackzz
#@software: PyCharm
#@time: 2019/5/30 11:43

from  django import  forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=20)
    password = forms.CharField(label='密码',
                               max_length=8,
                               min_length=6,
                               widget=forms.PasswordInput(attrs={'placeholder':'请输入密码长度6到8位'}),
                               error_messages={
                                   'min_length':'密码长度小于6',
                                   'max_length':'密码长度大于8',
                               })
    password_repeat = forms.CharField(label='再次输入密码',widget=forms.PasswordInput())
    email = forms.EmailField()

    def clean(self):
        clean_data = super().clean() #继承父类

        #增加提示信息功能add_error（字段名，提示信息）
        password = clean_data.get('password')
        password_repeat = clean_data.get('password_repeat')
        if password_repeat != password:
            self.add_error('password_repeat','密码不一致')
