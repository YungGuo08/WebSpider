# @Author: Yun
# @Time  : 2020/9/13 22:56


import requests
import json
import time
import threading
from queue import Queue
from pymongo import MongoClient

# 导入base64编码模块
from meituan._token import encode_token


class Meituan(object):

    def __init__(self):

        self.url = 'https://sz.meituan.com/meishi/api/poi/getPoiList?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
            'Referer': 'https://sz.meituan.com/meishi/'
        }
        # params队列
        self.params_queue = Queue()
        # 请求响应队列
        self.response_queue = Queue()
        # 保存的数据队列
        self.save_queue = Queue()
        # 初始化数据库
        self.client = MongoClient()
        self.db = self.client.hao123
        self.collection = self.db.meituan

    def save(self):
        """
        保存
        """
        while True:
            item = self.save_queue.get()
            self.collection.insert_one(item)
            self.client.close()
            self.save_queue.task_done()

    def parser(self):
        """
        解析
        """
        while True:
            data_list = self.response_queue.get()
            for data in data_list:
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
                self.save_queue.put(item)
            self.response_queue.task_done()

    def get_page(self):
        """
        请求
        """
        while True:
            params = self.params_queue.get()
            response = requests.get(self.url, headers=self.headers, params=params)
            data_list = json.loads(response.content.decode())['data']['poiInfos']
            self.response_queue.put(data_list)
            self.params_queue.task_done()

    def param(self):
        """
        参数
        """
        for page in range(1, 68):
            sign = encode_token(str(f'areaId=0&cateId=0&cityName=深圳&dinnerCountAttrId=&optimusCode=10&'
                                    f'originUrl=https://sz.meituan.com/meishi/pn{page}/&page=1&partner=126&platform=1&'
                                    f'riskLevel=1&sort=rating&userId=&uuid=709d0c8af39f43fbb198.1599978102.1.0.0'))
            ts = int(time.time() * 1000)
            token_data = {
                "rId": 100900,
                "ver": "1.0.6",
                "ts": ts,
                "cts": ts + 100,
                "brVD": [1920, 324],
                "brR": [[1920, 1080], [1920, 1040], 24, 24],
                "bI": [f"https://sz.meituan.com/meishi/pn{page}/", ""],
                "mT": [],
                "kT": [],
                "aT": [],
                "tT": [],
                "aM": "",
                "sign": sign
            }
            # 将token_data编码为base64
            _token = encode_token(str(token_data))
            params = {
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
                '_token': _token,
            }
            self.params_queue.put(params)

    def run(self):
        self.param()
        # 多线程
        thread_list = []
        for i in range(10):
            get_page = threading.Thread(target=self.get_page)
            thread_list.append(get_page)

        for i in range(10):
            parser = threading.Thread(target=self.parser)
            thread_list.append(parser)

        for i in range(10):
            save = threading.Thread(target=self.save)
            thread_list.append(save)

        for thread in thread_list:
            thread.setDaemon(True)
            thread.start()

        for i in [self.params_queue, self.response_queue, self.save_queue]:
            i.join()


if __name__ == '__main__':
    run_time = time.time()
    meituan = Meituan()
    meituan.run()
    end_time = time.time()
    print(f'爬取完成！用时：{end_time - run_time}秒')
