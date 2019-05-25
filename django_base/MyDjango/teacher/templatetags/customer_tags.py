#!/usr/bin/env python
# encoding: utf-8
#@author: jack
#@contact: 935650354@qq.com
#@site: https://www.cnblogs.com/jackzz
#@software: PyCharm
#@time: 2019/5/16 0016 下午 23:34
from datetime import datetime
from django import template
register = template.Library()


@register.simple_tag(name='current', takes_context=True)#
def current_time(context):
    return datetime.now().strftime(context['format_str'])\




@register.inclusion_tag('teacher/show_list.html')
def show_list(value, style):
    return {'ls': value, 'style': style}



# def current_time(context):
#     return datetime.now().strftime(context['format_str'])