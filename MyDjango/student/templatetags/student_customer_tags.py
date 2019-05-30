#!/usr/bin/env python
# encoding: utf-8
#@author: jack
#@contact: 935650354@qq.com
#@site: https://www.cnblogs.com/jackzz
#@software: PyCharm
#@time: 2019/5/29 22:08


from  django import  template

register = template.Library()

@register.inclusion_tag('student/pagnitor.html',takes_context=True)
def pagination_html(context):
    total_page = context['total_page']
    page = context['page']
    # page_list = context['p'].page_range
    page_list = []
    num = 1
    if page - num <=0:
        for i in range(1,page + 1):
            page_list.append(i)
    else:
        for i in range(page - num,page + 1):
            page_list.append(i)
    if page + num >= total_page:
        for i in range(page + 1,total_page + 1):
            page_list.append(i)
    else:
        for i in range(page + 1,num + 1):
            page_list.append(i)

    return {
        'total_page':total_page,
        'page_list':page_list,
        'page':page,
        'per_page':context['per_page'],
    }

@register.simple_tag()
def add_class(field,class_str):
    return field.as_widget(attrs={'class':class_str})