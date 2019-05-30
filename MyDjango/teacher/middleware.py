#!/usr/bin/env python
# encoding: utf-8
#@author: jack
#@contact: 935650354@qq.com
#@site: https://www.cnblogs.com/jackzz
#@software: PyCharm
#@time: 2019/5/30 19:11

from django.http import HttpResponseForbidden

def simple_middleware(get_response): #参数固定
    print("一次性设置和初始化1")

    def middleware(request):
        user_agent = request.META['HTTP_USER_AGENT']
        if not 'chrome' in user_agent.lower():
            return HttpResponseForbidden()
        print('处理请求之前执行的代码2')

        response = get_response(request)

        print("处理请求、响应之后的代码5")
        return response
    return middleware

class SimpleMiddleWare:
    def __init__(self,get_response):
        self.get_response = get_response
        print("一次性设置和初始化0")

    def __call__(self, request):
        print('处理请求之前执行的代码3')

        response = self.get_response(request)

        print("处理请求、响应之后的代码4")
        return response
