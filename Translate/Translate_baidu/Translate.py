import requests
import re
import execjs
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from .Setting import FROM_LANGUAGE, TO_LANGUAGE, TRANS_TYPE

# 关闭ssl验证错误提醒
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class FanYi(object):

    def __init__(self, keyword):

        self.keyword = keyword
        self.url = ['https://fanyi.baidu.com/?aldtype=16047',
                    f'https://fanyi.baidu.com/v2transapi?']
        self.session = requests.session()
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
            'referer': 'https://fanyi.baidu.com/?aldtype=16047',
            'origin': 'https://fanyi.baidu.com',
        }

    def key_parameter(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
        }
        response = self.session.get(self.url[0], headers=headers, verify=False).content.decode()
        # 获取页面中的token/gtk
        token = re.findall(r'token: \'(.*?)\',', response)[0]
        gtk = re.findall(r'window.gtk = \'(.*?)\';', response)[0]
        # 读取js
        with open('sign_baidu.js', 'r') as f:
            js = f.read()
        # 生成js对象
        exec_obj = execjs.compile(js)
        # 调用js中的sign方法并传入参数生成sign
        sign = exec_obj.call("sign", self.keyword, gtk)
        return token, sign

    def form_data(self, token, sign):
        data = {
            'from': FROM_LANGUAGE,
            'to': TO_LANGUAGE,
            'query': self.keyword,
            'transtype': TRANS_TYPE,
            'simple_means_flag': 3,
            'sign': sign,
            'token': token,
            'domain': 'common'
        }
        return data

    def run(self):
        try:
            # 调用两次key_parameter函数以保证token为最新的，否则请求不到数据
            self.key_parameter()
            token, sign = self.key_parameter()
            form_data = self.form_data(token, sign)
            data = self.session.post(self.url[1], headers=self.headers, data=form_data, verify=False).json()
            result = data['trans_result']['data'][0]['dst']
            print('翻译结果:', result)
        except:
            print(f'翻译失败，请稍后重试或查看翻译设置是否正确！')


if __name__ == '__main__':
    word = input('请输入原文: ')
    fy = FanYi(word)
    fy.run()
