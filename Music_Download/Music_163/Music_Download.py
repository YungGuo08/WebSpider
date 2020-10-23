import random
import requests
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from Music_163.Encryption import AES_Encrypt, Encrypt_String, Random_String
from Music_163.Setting import SAVE_ADDRESS, KEY, FIXED_VALUE, IV, HEADERS

# 关闭ssl验证错误提醒
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Music_Download(object):

    def __init__(self, keyword):
        # 加密固定key参数
        self.key = KEY
        # 加密固定值参数
        self.fixed_value = FIXED_VALUE
        # 加密偏移量参数
        self.iv = IV
        # 接口关键参数（需要加密的字符串）
        self.key_parameter = r'{"hlpretag":"<span class=\"s-fc7\">","hlposttag":"</span>","s":"' + keyword + \
                             r'","type":"1","offset":"0","total":"true","limit":"30","csrf_token":""}'
        # 搜索页接口、music下载接口
        self.url = ['https://music.163.com/weapi/cloudsearch/get/web?csrf_token=',
                    'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=']
        self.headers = HEADERS

    def save(self, data, info):
        """
        保存
        :param data: music
        :param info: music信息
        :return:
        """
        with open(f"{SAVE_ADDRESS}{info['music_name']}-{info['singer']}.m4a", 'wb') as f:
            f.write(data)

    def encrypt(self):
        """
        加密params/encSecKey
        :return: 返回需要传递的data
        """
        # 使用固定key进行第一次AES加密
        param = AES_Encrypt(self.key, self.iv, self.key_parameter)
        # 生成随机key
        random_key = Random_String()
        # 使用随机key进行二次加密
        params = AES_Encrypt(random_key, self.iv, param)
        # 加密encSecKey
        encSecKey = Encrypt_String(self.fixed_value, random_key)
        form_data = {
            "params": params,
            "encSecKey": encSecKey
        }
        return form_data

    def post_page(self, url, form_data):
        """
        post请求页面
        :param url: 接口url
        :param form_data: 需要传递的data
        :return: 返回响应内容
        """
        # 设置了1秒内随机等待，速度太快可能会导致获取不到数据
        time.sleep(random.random())
        response = requests.post(url, headers=self.headers, data=form_data, verify=False)
        return response.json()

    def parser_search(self):
        """
        解析搜索结果数据
        :return: 返回歌曲信息
        """
        search_info = {}
        data = self.post_page(self.url[0], self.encrypt())['result']
        print('-' * 50)
        print(f"本次共找到{data['songCount']}首歌曲：")
        count = 0
        for info in data['songs']:
            # 歌曲id
            search_info['music_id'] = info['id']
            # 歌名
            search_info['music_name'] = info['name']
            # 歌手名
            search_info['singer'] = info['ar'][0]['name']
            print(f"【{count}】[歌名]：{search_info['music_name']} | [歌手]：{search_info['singer']}")
            count += 1
        print('-' * 50)
        select = int(input('请输入对应数字下载：'))
        result = {}
        # id
        result['id'] = data['songs'][select]['id']
        # 歌名
        result['music_name'] = data['songs'][select]['name']
        # 歌手名
        result['singer'] = data['songs'][select]['ar'][0]['name']
        return result

    def parser_music(self, music_id):
        """
        解析歌曲页
        :param music_id: 歌曲id
        :return: 返回歌曲下载url
        """
        # music接口关键参数
        self.key_parameter = r'{"ids":"[' + str(music_id) + r']","level":"standard","encodeType":"aac","csrf_token":""}'
        music_data = self.post_page(self.url[1], self.encrypt())['data'][0]
        music_url = music_data['url']
        if music_url is None:
            print('此歌曲为vip歌曲，无法下载！')
            # 程序终止
            exit()
        else:
            return music_url

    def run(self):
        try:
            # 解析搜索页
            result_info = self.parser_search()
            # 解析歌曲页
            music_url = self.parser_music(result_info['id'])
            # 下载music
            response = requests.get(music_url, headers=self.headers)
            # 保存
            self.save(response.content, result_info)
            print('下载完成！')
        except Exception as e:
            print(f'出现错误：{e}，请稍后重新运行！')


if __name__ == '__main__':
    key_word = input('请输入歌名：')
    music = Music_Download(key_word)
    music.run()
