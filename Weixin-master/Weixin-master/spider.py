from urllib.parse import urlencode
import pymongo
import requests
from lxml.etree import XMLSyntaxError
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq
from config import *

client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DB]


base_url = 'http://weixin.sogou.com/weixin?'

headers = {
    # 'Cookie': 'SUID=F6177C7B3220910A000000058E4D679; SUV=1491392122762346; ABTEST=1|1491392129|v1; SNUID=0DED8681FBFEB69230E6BF3DFB2F8D6B; ld=OZllllllll2Yi2balllllV06C77lllllWTZgdkllll9lllllxv7ll5@@@@@@@@@@; LSTMV=189%2C31; LCLKINT=1805; weixinIndexVisited=1; SUIR=0DED8681FBFEB69230E6BF3DFB2F8D6B; JSESSIONID=aaa-BcHIDk9xYdr4odFSv; PHPSESSID=afohijek3ju93ab6l0eqeph902; sct=21; IPLOC=CN; ppinf=5|1491580643|1492790243|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToyNzolRTUlQjQlOTQlRTUlQkElODYlRTYlODklOER8Y3J0OjEwOjE0OTE1ODA2NDN8cmVmbmljazoyNzolRTUlQjQlOTQlRTUlQkElODYlRTYlODklOER8dXNlcmlkOjQ0Om85dDJsdUJfZWVYOGRqSjRKN0xhNlBta0RJODRAd2VpeGluLnNvaHUuY29tfA; pprdig=j7ojfJRegMrYrl96LmzUhNq-RujAWyuXT_H3xZba8nNtaj7NKA5d0ORq-yoqedkBg4USxLzmbUMnIVsCUjFciRnHDPJ6TyNrurEdWT_LvHsQIKkygfLJH-U2MJvhwtHuW09enCEzcDAA_GdjwX6_-_fqTJuv9w9Gsw4rF9xfGf4; sgid=; ppmdig=1491580643000000d6ae8b0ebe76bbd1844c993d1ff47cea',
    'Cookie': 'SUV=00013A1F6E5A8CE95C5EC859BC8FF739; sw_uuid=3731781510; ssuid=2561449552; CXID=1ECBF9627D98C7103A1CC4FA78795793; IPLOC=CN3509; SUID=21AB23781E20910A000000005CA0A3EF; ABTEST=0|1555986927|v1; __guid=14337457.3555022097284861000.1555986956094.465; weixinIndexVisited=1; JSESSIONID=aaaB6u-Wviri88-WK60Ow; ppinf=5|1555999641|1557209241|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo2MzolRTYlQjUlODElRTYlQjUlQUElRTUlODglQjAlRTUlQjIlODElRTYlOUMlODglRTYlOUUlQUYlRTklQkIlODR8Y3J0OjEwOjE1NTU5OTk2NDF8cmVmbmljazo2MzolRTYlQjUlODElRTYlQjUlQUElRTUlODglQjAlRTUlQjIlODElRTYlOUMlODglRTYlOUUlQUYlRTklQkIlODR8dXNlcmlkOjQ0Om85dDJsdUdheVg4aXN6Ui1YM1F4WnNEOHdMdk1Ad2VpeGluLnNvaHUuY29tfA; pprdig=YZBnKbx8pJJGs0nfYaWipDIgyaxl60Iifo6UxiYC800nstfn-AyGjr272orodgvao_hpeb34weaOpIvu8_IX7reXZT66h_bGd4_-D5bHd7xJJ2Vnp8VbW12HLF6i68Ts7qahQWF_bKEAMkfeGpfSUeXmrXAs29VYQZQStUALceA; sgid=09-40254237-AVyibq5nWwI2Cq08GzErHfyY; ppmdig=155599964200000021e33d1c19da0272b5228e103d19a923; PHPSESSID=0r8c22e4ij9map60b0f7cfnkm5; seccodeErrorCount=1|Tue, 23 Apr 2019 06:13:08 GMT; SNUID=DA4E5ED9C1C445EDAA8621D2C2F9F23E; seccodeRight=success; successCount=1|Tue, 23 Apr 2019 06:13:30 GMT; monitor_count=10',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

proxy = None


def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

def get_html(url, count=1):
    print('Crawling', url)
    print('Trying Count', count)
    global proxy
    if count >= MAX_COUNT:
        print('Tried Too Many Counts')
        return None
    try:
        if proxy:
            proxies = {
                'http': 'http://' + proxy
            }
            response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            # Need Proxy
            print('302')
            proxy = get_proxy()
            if proxy:
                print('Using Proxy', proxy)
                return get_html(url)
            else:
                print('Get Proxy Failed')
                return None
    except ConnectionError as e:
        print('Error Occurred', e.args)
        proxy = get_proxy()
        count += 1
        return get_html(url, count)



def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html

def parse_index(html):
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')

def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

def parse_detail(html):
    try:
        doc = pq(html)
        print(doc)
        title = doc('.rich_media_title').text()
        content = doc('.rich_media_content').text()
        date = doc('#post-date').text()
        nickname = doc('#js_profile_qrcode > div > strong').text()
        wechat = doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        return {
            'title': title,
            'content': content,
            'date': date,
            'nickname': nickname,
            'wechat': wechat
        }
    except XMLSyntaxError:
        return None

def save_to_mongo(data):
    if db['articles'].update({'title': data['title']}, {'$set': data}, True):
        print('Saved to Mongo', data['title'])
    else:
        print('Saved to Mongo Failed', data['title'])


def main():
    for page in range(1, 101):
        html = get_index(KEYWORD, page)
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                article_html = get_detail(article_url)
                if article_html:
                    article_data = parse_detail(article_html)
                    print(article_data)
                    if article_data:
                        save_to_mongo(article_data)



if __name__ == '__main__':
    main()
