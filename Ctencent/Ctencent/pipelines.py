# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from Ctencent.items import CtencentItem,DtencentItem

class CtencentPipeline(object):
    def open_spider(self,spider):
        self.file =open(r'menu_info.json','w',encoding='utf')

    def process_item(self, item, spider):
        if isinstance(item,CtencentItem):#判断item是否是CtencentItem
            content = json.dumps(dict(item),ensure_ascii=False)+'\n'
            self.file.write(content)
        return item

    def close_spider(self,spider):
        self.file.close()



class DtencentPipeline(object):
    def open_spider(self,spider):
        self.file =open(r'detail_info.json','w',encoding='utf')

    def process_item(self, item, spider):
        if isinstance(item,DtencentItem):#判断item是否是DtencentItem
            content = json.dumps(dict(item),ensure_ascii=False)+'\n'
            self.file.write(content)
        return item

    def close_spider(self,spider):
        self.file.close()
