# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CtencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position_name = scrapy.Field()  # 职位名称
    position_type = scrapy.Field()  # 职位类别
    detail_url = scrapy.Field() #职位详情
    people_count = scrapy.Field()#招聘人数
    work_city = scrapy.Field() #工作地点
    release_date = scrapy.Field()  # 发布时间

class DtencentItem(scrapy.Item):
    job_description = scrapy.Field()  # 工作描述
    job_require = scrapy.Field()  # 工作要求
