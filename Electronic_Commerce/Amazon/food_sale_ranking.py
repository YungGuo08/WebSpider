import requests
import csv
from lxml import etree
from tqdm import tqdm


class Amazon:

    def __init__(self, page):

        self.url = f'https://www.amazon.com/-/zh/销售排行榜-Grocery-Gourmet-Food' \
                   f'/zgbs/grocery/ref=zg_bs_pg_{page}?_encoding=UTF8&pg={page}'

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/85.0.4183.102 Safari/537.36'
        }

    def run(self):
        response = requests.get(self.url, headers=self.headers)
        selector = etree.HTML(response.text)
        grocery_list = selector.xpath('//*[@id="zg-ordered-list"]/li/span/div')
        for grocery in tqdm(grocery_list, '进度：'):
            item = []
            # 排名
            ranking = grocery.xpath('div/span[1]/span/text()')[0]
            # 商品标题
            title = grocery.xpath('span/a/div/text()')[0].replace('\n', '').strip()
            try:
                # 星级
                star_rating = grocery.xpath('span/div[1]/a[1]/i/span/text()')[0].replace(' ', '')
            except:
                star_rating = ''
            try:
                # 评论数
                comments_number = grocery.xpath('span/div[1]/a[2]/text()')[0]
            except:
                comments_number = ''
            try:
                # 价格
                price = grocery.xpath('string(span/div[2]/a/span)').replace('US', '').replace(' ', '')
            except:
                price = ''
            # 商品url
            grocery_url = 'https://www.amazon.com' + grocery.xpath('span/a/@href')[0]
            item.extend([ranking, title, star_rating, comments_number, price, grocery_url])
            with open('../other/Amazon.csv', 'a', encoding='gbk', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(item)


if __name__ == '__main__':
    for i in range(1, 3):
        amazon = Amazon(i)
        amazon.run()

