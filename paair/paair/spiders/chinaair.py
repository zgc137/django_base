# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from paair.items import PaairItem

# class ChinaairSpider(CrawlSpider):
#     '''
#     1、访问首页https://www.aqistudy.cn/historydata/获取源代码，抽取每个城市url
#     2、访问每个城市url，再获取每个月份url
#     3、通过selenium访问每个月份的url，从加载后的源代码中提取当月当天的空气信息
#     4、提交item到管道，然后写入到json/数据库中
#     '''
#     name = 'chinaair'
#     allowed_domains = ['aqistudy.cn']
#     start_urls = ['https://www.aqistudy.cn/historydata/']
#     front_url = "https://www.aqistudy.cn/historydata/"
#
#     rules = (
#         Rule(LinkExtractor(allow=r'monthdata\.php', restrict_xpaths="//div[@class='all']//a"),
#              callback='parse_item', follow=False),
#     )
#
#     def parse_item(self, response):
#         '''
#         parse_item:要做2个事情
#         1、抽取城市URL和城市名称
#         2、跟进详情页面请求（每个月的url）
#         :param response:每个城市的response，包含该城市每个月份的Link
#         :return:
#         '''
#
#         city_url = response.url
#         city_name = response.meta["link_text"]
#         next_url_list = response.xpath("//ul[@class='unstyled']//a/@href").extract()
#         for next_url in next_url_list:
#             item = PaairItem()
#             item["city_name"] = city_name
#             item["city_url"] = city_url
#             yield scrapy.Request(url=self.font_url + next_url, callback=self.parse_detail,
#                                  meta={"item": item})
#
#     def parse_detail(self, response):
#         item = response.meta["item"]
#         node_list = response.xpath("//tbody//tr")[1:]#切片剔除表头内容
#         for node in node_list:
#             item["release_date"] = node.xpath("./td[1]/text()").extract_first()
#             item["air_AQI"] = node.xpath("./td[2]/text()").extract_first()
#             item["air_quality"] = node.xpath("./td[3]/span/text()").extract_first()
#             item["air_PM2_5"] = node.xpath("./td[4]/text()").extract_first()
#             item["air_PM10"] = node.xpath("./td[5]/text()").extract_first()
#             item["air_SO2"] = node.xpath("./td[6]/text()").extract_first()
#             item["air_CO"] = node.xpath("./td[7]/text()").extract_first()
#             item["air_NO2"] = node.xpath("./td[8]/text()").extract_first()
#             item["air_O3_8h"] = node.xpath("./td[9]/text()").extract_first()
#             yield item
#
class ChinaSpider(CrawlSpider):
    """
    1. 访问https://www.aqistudy.cn/historydata/ 获取首页源代码, 抽取每个城市的url
    2. 访问每个城市的url, 再从获取每个月份的url.
    3. 通过selenium访问每个月份的url, 从加载后的源代码中获取当月每天的空气质量信息.
    4. 提交Item到管道, 然后写入到json文件中.
    """
    name = 'chinaair'
    allowed_domains = ['aqistudy.cn']
    start_urls = ['https://www.aqistudy.cn/historydata/']
    font_url = "https://www.aqistudy.cn/historydata/"

    rules = (
        Rule(LinkExtractor(allow=r'monthdata\.php', restrict_xpaths="//div[@class='all']//a"),
             callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        """
        `parse_item`要做两个事情
        1. 获取城市url和城市名称
        2. 跟进详情页的请求.(每个月的url)
        :param response: 每个城市的response, 包含该城市每个月份的link
        :return:
        """
        city_url = response.url
        city_name = response.meta["link_text"]
        next_url_list = response.xpath("//ul[@class='unstyled1']//a/@href").extract()
        for next_url in next_url_list:
            item = PaairItem()
            item["city_name"] = city_name
            item["city_url"] = city_url
            yield scrapy.Request(url=self.font_url + next_url, callback=self.parse_detail,
                                 meta={"item": item})

    def parse_detail(self, response):
        item = response.meta["item"]
        node_list = response.xpath("//tbody//tr")[1:]
        for node in node_list:
            item["release_date"] = node.xpath("./td[1]/text()").extract_first()
            item["air_AQI"] = node.xpath("./td[2]/text()").extract_first()
            item["air_quality"] = node.xpath("./td[3]/span/text()").extract_first()
            item["air_PM2_5"] = node.xpath("./td[4]/text()").extract_first()
            item["air_PM10"] = node.xpath("./td[5]/text()").extract_first()
            item["air_SO2"] = node.xpath("./td[6]/text()").extract_first()
            item["air_CO"] = node.xpath("./td[7]/text()").extract_first()
            item["air_NO2"] = node.xpath("./td[8]/text()").extract_first()
            item["air_O3_8h"] = node.xpath("./td[9]/text()").extract_first()
            yield item


