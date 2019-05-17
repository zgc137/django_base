# -*- coding: utf-8 -*-
import scrapy
from patimo.items import PatimoItem

class TimoSpider(scrapy.Spider):
    name = 'timo'
    allowed_domains = ['image.baidu.com']
    # start_urls = ['http://image.baidu.com/']
    word = input("请输入你想要获取的图片： ")
    # start_urls = ['http://image.baidu.com/search/index?tn=baiduimage&ie=utf-8&word='+word]
    start_urls = ['http://image.baidu.com/search/index?tn=baiduimage&word='+word]
    #作业我输入的是：冯提莫图片见images
    def parse(self, response):
        item = PatimoItem()
        # item["image_urls"] = response.xpath("//div[@class='imglist clearfix pageNum0']//img/@src").extract()
        item["image_urls"] = response.xpath("//div[@id='imgid']//img/@src").extract()
        yield item
