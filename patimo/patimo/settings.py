# -*- coding: utf-8 -*-

# Scrapy settings for patimo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'patimo'

SPIDER_MODULES = ['patimo.spiders']
NEWSPIDER_MODULE = 'patimo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'patimo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # 'Accept':'application/json, text/javascript, */*; q=0.01',
    # 'Accept-Encoding':'gzip, deflate',
    # 'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Connection':'keep-alive',
    # 'Cookie':'BAIDUID=32BDD69043474BF5DF07E7943E2A72FC:FG=1; BIDUPSID=32BDD69043474BF5DF07E7943E2A72FC; PSTM=1549627055; __guid=53209008.925268832825741800.1549978193261.2974; MCITY=-340%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=ks4U09LdFYzNkVoaFliRkVHLXZabk1aNHI4fjF0R1FxZjdZLUdBY2lVZzVHZXBjSUFBQUFBJCQAAAAAAAAAAAEAAABH~Io1wbXJz7r8wOrDw9fTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADmMwlw5jMJcN; H_PS_PSSID=1434_21081_28774_28721_28833_28585_28604; indexPageSugList=%5B%22%E5%86%AF%E6%8F%90%E8%8E%AB%22%2C%22%E5%9B%BE%E7%89%87%E5%A6%B9%E5%AD%90%22%2C%22%E5%A3%81%E7%BA%B8%22%2C%22%E5%86%AF%E6%8F%90%E8%8E%AB%E6%9D%9C%E8%95%BE%E6%96%AF%20%E5%86%99%E7%9C%9F%22%5D; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=www.baidu.com; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; firstShowTip=1; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; monitor_count=19',
    # 'Host':'image.baidu.com',
    'Referer':'http：//image.baidu.com/search/index?tn=baiduimage&word=%E5%86%AF%E6%8F%90%E8%8E%AB',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    # 'X-Requested-With':'XMLHttpRequest'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'patimo.middlewares.PatimoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'patimo.middlewares.PatimoDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'patimo.middlewares.ChromeDynamicMiddleware': 544,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 1. 需要启动内置的图片管道.
    'scrapy.pipelines.images.ImagesPipeline': 1,
    # 'patimo.pipelines.PatimoImagesPipeline': 300,

}
# 2. 需要指定图片文件保存路径.
IMAGES_STORE ='D:\study\patimo\patimo\images'
# 生成指定格式的缩略图
IMAGES_THUMBS = {
   "small": (50, 50),
   "big": (110, 110),
}



# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
