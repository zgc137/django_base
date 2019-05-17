# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PaairItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 城市的名字
    city_name = scrapy.Field()
    # 城市的url
    city_url = scrapy.Field()

    # 日期	AQI	质量等级	PM2.5	PM10	SO2	CO	NO2	O3_8h
    release_date = scrapy.Field()
    # AQI
    air_AQI = scrapy.Field()
    # 质量等级
    air_quality = scrapy.Field()
    # PM2.5
    air_PM2_5 = scrapy.Field()
    # PM10
    air_PM10 = scrapy.Field()
    # SO2
    air_SO2 = scrapy.Field()
    # CO
    air_CO = scrapy.Field()
    # NO2
    air_NO2 = scrapy.Field()
    # O3_8h
    air_O3_8h = scrapy.Field()



