# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from patimo.user_agents import agents
from scrapy import signals
from time import sleep
import random,scrapy
from selenium import webdriver

class PatimoSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class PatimoDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        # 1. 使用随机函数, 从序列中获取UA数据
        agent = random.choice(agents)
        # 2. 将数据赋值给请求头部.
        request.headers["User-Agent"] = agent
        return None


class ChromeDynamicMiddleware(object):
    def process_request(self, request, spider):
        """
        request对象可能是
        1. 爬虫文件跟进的请求
        2. 爬虫文件start_urls的请求
        3. 中间件类中返回的请求.

        反正请求流到中间件的时候, process_request就会去处理这些请求, 怎么处理看你中间件代码怎么写.
        在这里, 请求流到了这里, 先进行if条件判断, 若当前请求的url是小说书库的第一页(http://www.xs4.cc/shuku/)的话.
        我就用selenium来访问这个url, 然后获取动态加载的数据, 然后构造response返回给引擎.
        若流过来的请求的url不是(http://www.xs4.cc/shuku/), 那就直接return None, 交给其他中间件处理, 我反正是不管了.

        selenium访问请求的headers是什么?我用的chrome, chrome该携带什么headers, selenium自己就携带什么.
        selenium发送的请求 到 获取到数据, 都是在一个方法中就完成,  跟其他中间件有什么关系?

        :param request:
        :param spider:
        :return:
        """
        # 1. 判断请求是否是目标请求
        url = "http://image.baidu.com/search/index?tn=baiduimage&word=%E5%86%AF%E6%8F%90%E8%8E%AB"
        if request.url == url:
            # 创建浏览器设置对象, 可设置相关参数如以无界面方式运行driver.
            opts = webdriver.ChromeOptions()
            opts.add_argument("--headless")
            # 2. 创建对应的浏览器driver对象, 应用设置对象
            driver = webdriver.Chrome()
            # 3. 通过driver对象访问页面, 获取渲染后的动态数据.
            driver.get(request.url)
            # 4. 由于访问可能存在不确定因素, 如网络延迟, 所以等待浏览器加载页面数据需要一定时间.
            sleep(5)
            # 5. 通过driver对象获取加载后的页面数据
            html_data = driver.page_source
            # 6. 使用完driver对象需进行退出.
            driver.quit()
            # 7. 构造响应对象并返回.
            return scrapy.http.HtmlResponse(url=url,body=html_data,request=request,encoding="utf-8")
        else:
            # 若不是目标请求就返回None.
            return None