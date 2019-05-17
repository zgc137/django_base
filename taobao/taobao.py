import re,requests
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *
import pymongo

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


# 进入浏览器设置
options = webdriver.ChromeOptions()


options.add_argument('upgrade=insecure-requests: 1')
# 更换头部
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"')

browser = webdriver.Chrome(chrome_options=options)
wait = WebDriverWait(browser,2000)


def search():
    try:
        browser.get('https://www.taobao.com/?')
        search_windows = browser.current_window_handle
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#q'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
        input.clear()
        input.send_keys('美食')
        submit.click()
        browser.switch_to.window(search_windows)

        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total')))
        get_products()
        return  total.text
    except TimeoutException:
        return search()

def next_page(page_number):
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span')))
        get_products()
    except TimeoutException:
        next_page(page_number)
def get_products():
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc =pq(html)
    items = doc('mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image':item.find('.pic .img').attr('src'),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text()[:-3],
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text(),
        }
        print(product)
        save_to_mongo(product)

def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('save to mongo sucess',result)
    except Exception:
        print('save to mongo fail',result)
def main():
    total = search()
    total = int(re.compile('(\d+)').search(total).group(1))
    for i in range(2,total + 1):
        next_page(i)


if __name__ == '__main__':
    main()