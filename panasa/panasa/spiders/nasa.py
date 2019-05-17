# -*- coding: utf-8 -*-
import scrapy
from panasa.items import PanasaItem


class NasaSpider(scrapy.Spider):
    name = 'nasa'
    # allowed_domains = ['nasa.gov']
    allowed_domains = ['baidu.com']
    start_urls = ['http://image.baidu.com/']

    def parse(self, response):
        item = PanasaItem()
        item["image_urls"] = response.xpath("//div[@id='imglist']//img/@src").extract()
        yield item
