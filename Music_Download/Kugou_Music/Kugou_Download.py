"""
1、仅支持下载非vip歌曲，由于是利用酷狗的歌曲播放接口下载，能下载到的vip歌曲是试听版的；
2、默认下载搜索结果中第一首歌曲；
3、如果酷狗没有该歌曲，只要搜索到的列表中有歌曲（酷狗会将和关键词相关的歌曲放到列表），都会下载第一首歌曲。
"""

import time
import hashlib
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 关闭ssl验证错误提醒
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Kugou_Music(object):

    def __init__(self, keyword):
        # 搜索接口
        self.url = 'https://complexsearch.kugou.com/v2/search/song?'

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
        }
        # 时间戳
        self.time_1 = int(time.time() * 1000)
        self.time_2 = int(time.time() * 1000)
        # 关键字符串参数
        self.signature = f'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtclientver=2000dfid=-keyword={keyword}mid={self.time_2}' \
                         f'page=1pagesize=30platform=WebFiltersrcappid=2919userid=-1NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'
        # 歌曲保存地址
        self.address = './'

    def save(self, music_info, data):
        """
        保存
        :param music_info: 歌曲信息
        :param data: 歌曲
        :return:
        """
        with open(f"{self.address}{music_info['music_name']}-{music_info['singer']}.mp3", 'wb') as f:
            f.write(data.content)

    def param(self):
        """
        参数
        :return:
        """
        # 将关键字符串加密
        hash_ = hashlib.md5()
        hash_.update(self.signature.encode())
        result = hash_.hexdigest().upper()
        params = {
            'keyword': word,
            'page': 1,
            'pagesize': 30,
            'platform': 'WebFilter',
            'userid': -1,
            'clientver': 2000,
            'srcappid': 2919,
            'mid': self.time_1,
            'dfid': '-',
            'signature': result,
        }
        return params

    def get_search_page(self, url, params):
        """
        搜索页面
        :param url:
        :param params:
        :return:
        """
        response = requests.get(url, headers=self.headers, params=params, verify=False).json()
        music_info = {}
        # 获取列表中的第一首歌曲信息
        data = response['data']['lists'][0]
        # 歌名
        music_info['music_name'] = data['SongName']
        # 歌手
        music_info['singer'] = data['SingerName']
        # 歌曲hash
        music_info['music_file'] = data['FileHash']
        return music_info

    def get_music_page(self, music_hash):
        """
        请求歌曲
        :param music_hash:
        :return:
        """
        # 歌曲接口
        music_info_url = f'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={music_hash}'
        # cookie中的kg_mid是必须参数，具体说明见kg_mid_generator文件
        cookie = {
            'kg_mid': 'aad44cc5d3cf31fe45f76e8c8561d8a3'
        }
        response = requests.get(music_info_url, headers=self.headers, cookies=cookie, verify=False).json()
        data = response['data']
        # 歌曲下载链接
        music_url = data['play_url']
        return music_url

    def run(self):
        try:
            # 参数生成
            params = self.param()
            # 获取歌曲信息
            music_info = self.get_search_page(self.url, params)
            # 获取下载链接
            music_url = self.get_music_page(music_info['music_file'])
            # 下载
            response = requests.get(music_url, headers=self.headers)
            self.save(music_info, response)
            print('下载完成！')
        except Exception as e:
            print(f'运行出错：{e}，请稍后重试！')


if __name__ == '__main__':
    word = input('请输入歌名：')
    music = Kugou_Music(word)
    music.run()
