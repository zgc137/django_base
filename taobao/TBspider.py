import requests,re
lst = [] #存放商品信息，以防重复

class TBSpider(): #淘宝爬虫类
    url = 'https://s.taobao.com/search'
    payload = {'q': 'python', 's': '1', 'ie': 'utf8'}  # 字典传递url参数
    file_name = 'tbdata.txt' #输出文件，就是csv格式，后缀名不是问题
    fl=None

    # 初始化，建立文件标题行，q为需要查询的物品信息
    def __init__(self,q=''):
        self.url='https://s.taobao.com/search'
        self.payload['q']=q
        self.fl = open(self.file_name,'w',encoding='utf-8')
        self.fl.writelines('"编号","标题","价格","产地","销售量","店铺"\n')

    #在结束时关闭文件
    def __del__(self):
        self.fl.close()

    #开始爬虫
    def start_spider(self):
        page_count = self.get_page_count('')
        for i in range(0,page_count):
            self.payload['s']=44*i #注意翻页技巧，根据URL自行判断
            resp = requests.get(self.url, params=self.payload)
            resp.encoding='utf-8'
            self.get_content(html=resp.text)
            print('Getting content ',i)


    def get_content(self,html):
        try:
            title = re.findall(r'"raw_title":"([^"]+)"', html, re.I)
            loc = re.findall(r'"item_loc":"([^"]+)"',html,re.I)
            price = re.findall(r'"view_price":"([^"]+)"', html, re.I)
            nid = re.findall(r'"nid":"([^"]+)"', html, re.I)
            sales = re.findall(r'"view_sales":"([^"]+)"', html, re.I)
            nick = re.findall(r'"nick":"([^"]+)"', html, re.I)
            k = len(title)
            for i in range(0,k):
                if nid[i] in lst:
                    continue
                lst.append(nid[i])
                p = sales[i][:-3]
                str = '"' + nid[i] + '",'
                str += '"' + title[i] + '",'
                str += '"' + price[i] + '",'
                str += '"' + loc[i] + '",'
                str += '"' + p + '",'
                str += '"' + nick[i] + '"\n'
                self.fl.writelines(str)
        except:
            print('Error ')

    def get_page_count(self,html):
        return 100

def main():
    q = '红酒真空瓶塞'
    spider = TBSpider(q=q)
    spider.start_spider()
    print('Total : ', len(lst))

main()

import pandas as pd
df = pd.read_csv('tbdata.txt')
df.head()