# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Ctencent.items import CtencentItem,DtencentItem


class CtencentSpider(CrawlSpider):
    name = 'ctencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']
    front_url = "https://hr.tencent.com/"
    #用来设置链接提取和url跟进
    rules = (
        #allow:正则表达式，用来匹配符合表达式要求的url，并且crawlspider会自动帮忙拼接成合法的url
        #callback:回调parse
        #follow：是否跟进后续符合要求的url,true跟进，False不跟进
        #1.第一个rule规则用于下一页数据获取和跟进
        Rule(LinkExtractor(allow=r'start=\d+#a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'position_detail.php'), callback='detail_parse', follow=False),
    )

    def parse_item(self, response):
        #xpath 获取节点对象
        tencenthr = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        #循环接收爬取数据
        for job in tencenthr:
            item = CtencentItem()
            item["position_name"] = job.xpath('.//a/text()').extract_first()
            item["detail_url"] = self.front_url + job.xpath('.//a/@href').extract_first()
            item["position_type"] = job.xpath('.//td[2]/text()').extract_first()
            item["people_count"] = job.xpath('.//td[3]/text()').extract_first()
            item["work_city"] = job.xpath('.//td[4]/text()').extract_first()
            item["release_date"] = job.xpath('.//td[5]/text()').extract_first()
            yield item

    def detail_parse(self, response):
        item = DtencentItem()
        node_list = response.xpath('//ul[@class="squareli"]')
        item["job_description"] = ''.join(node_list[0].xpath("./li/text()").extract())
        item["job_require"] = ''.join(node_list[1].xpath("./li/text()").extract())
        yield item


