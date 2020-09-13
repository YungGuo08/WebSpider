# @Author: Yun
# @Time  : 2020/9/13 14:29

import requests
import json
import time
from tqdm import tqdm
from pymongo import MongoClient

# 导入base64编码模块
from meituan._token import encode_token


class Meituan(object):

    def __init__(self, page):

        self.url = 'https://sz.meituan.com/meishi/api/poi/getPoiList?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
            'Referer': 'https://sz.meituan.com/meishi/'
        }
        self.sign = encode_token(str(f'areaId=0&cateId=0&cityName=深圳&dinnerCountAttrId=&optimusCode=10&'
                                     f'originUrl=https://sz.meituan.com/meishi/pn{page}/&page=1&partner=126&platform=1&'
                                     f'riskLevel=1&sort=rating&userId=&uuid=709d0c8af39f43fbb198.1599978102.1.0.0'))

        self.ts = int(time.time() * 1000)

        self.token_data = {
            "rId": 100900,
            "ver": "1.0.6",
            "ts": self.ts,
            "cts": self.ts + 100,
            "brVD": [1920, 324],
            "brR": [[1920, 1080], [1920, 1040], 24, 24],
            "bI": [f"https://sz.meituan.com/meishi/pn{page}/", ""],
            "mT": [],
            "kT": [],
            "aT": [],
            "tT": [],
            "aM": "",
            "sign": self.sign
        }
        self._token = encode_token(str(self.token_data))
        self.params = {
            'cityName': '深圳',
            'cateId': 0,
            'areaId': 0,
            'sort': 'rating',
            'dinnerCountAttrId': '',
            'page': page,
            'userId': '',
            'uuid': '709d0c8af39f43fbb198.1599978102.1.0.0',
            'platform': 1,
            'partner': 126,
            'originUrl': f'https://sz.meituan.com/meishi/pn{page}/',
            'riskLevel': 1,
            'optimusCode': 10,
            '_token': self._token,
        }
        self.client = MongoClient()
        self.db = self.client.hao123
        self.collection = self.db.meituan

    def save(self, item):

        self.collection.insert_one(item)

        self.client.close()

    def run(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        data_list = json.loads(response.content.decode())['data']['poiInfos']
        for data in tqdm(data_list, '进度：'):
            item = {}
            # 店铺id
            item['shop_id'] = data['poiId']
            # 店铺
            item['shop_name'] = data['title']
            # 评分
            item['avg_score'] = data['avgScore']
            # 评论数
            item['comments'] = data['allCommentNum']
            # 人均
            item['avg_price'] = data['avgPrice']
            # 地址
            item['address'] = data['address']
            self.save(item)


if __name__ == '__main__':
    run_time = time.time()
    for i in range(1, 68):
        print(f'爬取第{i}页：')
        meituan = Meituan(i)
        meituan.run()
    end_time = time.time()
    print(f'爬取完成！用时：{end_time - run_time}秒')
