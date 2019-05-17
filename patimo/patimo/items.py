# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PatimoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    '''
    这里需要创建image_urls, images字段, 这两个字段由于名字具有特殊性,
    会被图片管道识别, 并进行处理
    image_urls: 图片的URL
    images:主要是用来接收图片管道类处理后的相关信息。
    '''
    image_urls = scrapy.Field()
    images = scrapy.Field()