#!/usr/bin/env python
# encoding: utf-8
#@author: jack
#@contact: 935650354@qq.com
#@site: https://www.cnblogs.com/jackzz
#@software: PyCharm
#@time: 2019/5/24 0024 下午 22:17

from django import template
register = template.Library()
@register.filter()
def to_sex(value,arg='zh'):
    '''
    :param value: 0 or 1
    :param arg:
    :return:
    '''
    change = {
        'zh':('女','男'),
        'en':('Female','Male')
    }
    return change[arg][value]
# register.filter(to_sex)