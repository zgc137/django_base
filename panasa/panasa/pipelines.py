# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class PanasaPipeline(object):
    def process_item(self, item, spider):
        return item


class PanasaImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 返回给调度器整理入队, 再请求
        image_urls = item.get("image_urls", [])
        for image_url in image_urls:
            req = scrapy.Request(url=image_url)
            req.headers["Referer"] = "http://image.baidu.com/"
            yield req

    def item_completed(self, results, item, info):
        # file_paths = [x['path'] for ok, x in results if ok]
        file_paths = []
        # 打印返回结果中的文件路径信息
        for ok, x in results:
            if ok:
                file_paths.append(x['path'])
        return item
