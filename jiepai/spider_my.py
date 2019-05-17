# -*- coding: utf-8 -*-
# @Author  : Jackzz
import os
import re
from hashlib import md5
from json.decoder import JSONDecodeError
import pymongo
from config_my import *
import requests,json
from urllib.parse import  urlencode
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from multiprocessing import Pool

client = pymongo.MongoClient(MONGO_URL,connect=False)
db = client[MONGO_DB]

def get_page_index(offset,keyword):
    data = {
        "offset": offset,
        "format": "json",
        "keyword": keyword,
        "autoload": "true",
        "count": "20",
        "cur_tab": 3,
    }
    params = urlencode(data)
    base = 'http://www.toutiao.com/search_content/'
    url = base + '?' + params

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页错误')
        return None
def parse_page_index(text):
    try:
        data = json.loads(text)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('article_url')
    except JSONDecodeError:
        pass

def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('Error occurred')
        return None

def save_to_mongo(result):
    if db[MONGO_TABLE].insert[result]:
        print('Successfully Saved to Mongo',result)
        return True
    return False

def download_image(url):
    print('正在下载：',url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content)
        return None
    except RequestException:
        print('请求图片错误',url)
        return None
def save_image(content):
    file_path = '{0}/{1}/{2}'.format(os.getcwd(),md5(content).hexdigest(),'jpg')
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)
            f.close()



def main(offset):

    text = get_page_index(offset, KEYWORD)
    urls = parse_page_index(text)
    for url in urls:
        html = get_page_detail(url)
        result = parse_page_detail(html, url)
        if result: save_to_mongo(result)
        print(result)
    # html = get_page_index(offset, KEYWORD)
    # for url in parse_page_index(html):
    #     html = get_page_detail(url)
    #     if html:
    #         result = parse_page_detail(html,url)
    #         if result: save_to_mongo(result)
    # print(html)
def parse_page_detail(html,url):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    images_pattern = re.compile('gallery: JSON.parse\("(.*)"\)', re.S)
    result = re.search(images_pattern,html)
    if result:
        data = json.loads(result.group(1).replace('\\', ''))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get(url) for item in sub_images]
            for image in images: download_image(image)
            return {
                'title' : title,
                'url' : url,
                'images' : images

            }


if __name__ == '__main__':
    pool = Pool()
    groups = [x*20 for x in range(GROUP_START,GROUP_END+1)]
    pool.map(main, groups)
    pool.close()
    pool.join()

    # pool.map(main,groups)
