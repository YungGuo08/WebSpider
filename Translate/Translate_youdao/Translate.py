import requests
import time
import random
import string
import hashlib
from .Setting import ACTION, FROM_LANGUAGE, TO_LANGUAGE


class Fanyi(object):

    def __init__(self, keyword):

        self.keyword = keyword
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
            'referer': 'http://fanyi.youdao.com/'
        }
        self.cookie = {
            'OUTFOX_SEARCH_USER_ID': '103495734@10.169.0.84'
        }

    def form_data(self):
        # 时间戳
        time_1 = int(time.time() * 1000)
        # 时间戳+1位随机数
        time_2 = str(time_1) + ''.join(random.sample(string.digits, 1))
        # 组合关键参数
        sign_string = 'fanyideskweb' + self.keyword + time_2 + ']BjuETDhU)zqSxf-=B#7m'
        # 加密
        hash = hashlib.md5()
        hash.update(sign_string.encode())
        sign = hash.hexdigest()
        data = {
            'i': self.keyword,
            'from': FROM_LANGUAGE,
            'to': TO_LANGUAGE,
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': time_2,
            'sign': sign,
            'lts': time_1,
            'bv': '02edb5d6c6ac4286cd4393133e5aab14',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': ACTION
        }
        return data

    def run(self):
        try:
            form_data = self.form_data()
            response = requests.post(self.url, headers=self.headers, data=form_data, cookies=self.cookie).json()
            result = response['translateResult'][0][0]['tgt']
            print('翻译结果:', result)
        except:
            print('翻译失败，请检查翻译设置是否正确！')


if __name__ == '__main__':
    word = input('请输入原文: ')
    fanyi = Fanyi(word)
    fanyi.run()






