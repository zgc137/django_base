# -*- coding: utf-8 -*-
import scrapy
from hr_tencent.items import HrTencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']
    front_url = "https://hr.tencent.com/"
    def parse(self, response):

        tencenthr = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        for job in tencenthr:
            item = HrTencentItem()
            item["position_name"] = job.xpath('.//a/text()').extract_first()
            item["detail_url"] = self.front_url + job.xpath('.//a/@href').extract_first()
            item["position_type"] = job.xpath('.//td[2]/text()').extract_first()
            item["people_count"] = job.xpath('.//td[3]/text()').extract_first()
            item["work_city"] = job.xpath('.//td[4]/text()').extract_first()
            item["release_date"] = job.xpath('.//td[5]/text()').extract_first()
            yield scrapy.Request(url=item["detail_url"], callback=self.detail_parse, meta={"item": item})
        next_url = self.front_url + response.xpath('//div[@class="pagenav"]/a[@id="next"]/@href').extract_first()
        yield scrapy.Request(url=next_url, callback=self.parse)



    def detail_parse(self, response):
        item = response.meta["item"]
        node_list = response.xpath('//ul[@class="squareli"]')
        item["job_description"] = ''.join(node_list[0].xpath("./li/text()").extract())
        item["job_require"] = ''.join(node_list[1].xpath("./li/text()").extract())
        yield item
