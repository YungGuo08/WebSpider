import execjs
import requests
from QQ_Music.Setting import SAVE_ADDRESS

"""
1、仅支持下载非vip歌曲；
2、默认下载搜索到的列表中第一首歌曲；
3、如果是其它平台独家的歌曲，无法用此程序下载。
"""


class Music_Download(object):

    def __init__(self, keyword):
        # 搜索接口/歌曲页接口/下载接口
        self.url = ['https://c.y.qq.com/soso/fcgi-bin/client_search_cp?',
                    'https://u.y.qq.com/cgi-bin/musics.fcg?',
                    'https://ws.stream.qqmusic.qq.com/']
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
        }
        self.params = {
            'new_json': 1,
            'p': 1,
            'n': 10,
            'w': keyword,
            'format': 'json'
        }

    def save(self, music_info, music):
        """
        保存
        :param music_info: 歌曲信息
        :param music: 歌曲
        :return:
        """
        with open(f"{SAVE_ADDRESS}{music_info['music_name']}-{music_info['singer']}.m4a", 'wb') as f:
            f.write(music.content)

    def sign_generator(self, mid):
        """
        sign验证参数生成
        :param mid: 歌曲mid
        :return: 返回sign参数
        """
        # 读取js
        with open('sign.js', 'r') as f:
            data = f.read()
        # 生成js对象
        exec_obj = execjs.compile(data)
        # 调用js中的Sign方法并传入参数
        sign = exec_obj.call("Sign", mid)
        return sign

    def get_page(self, url, params):
        """
        请求页面
        :param url: 请求url
        :param params: 传递参数
        :return:
        """
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def parser_music(self, data):
        """
        解析歌曲页
        :param data: 歌曲页数据
        :return: 返回歌曲下载链接
        """
        data = data['req_0']['data']['midurlinfo'][0]
        if not len(data['purl']) == 0:
            # 获取歌曲下载链接
            music_url = self.url[2] + data['purl']
            return music_url
        else:
            print('未找到下载链接！（可能是vip歌曲）')
            exit()

    def parser_search(self, data):
        """
        解析搜索页
        :param data: 搜索页数据
        :return: 返回歌曲信息
        """
        music_info = {}
        data = data['data']['song']['list'][0]
        # 歌曲mid、歌名、歌手
        music_info['mid'] = data['mid']
        music_info['music_name'] = data['name']
        music_info['singer'] = data['singer'][0]['name']
        return music_info

    def run(self):
        try:
            # 获取搜索页数据
            search_result = self.get_page(self.url[0], self.params)
            print(search_result)
            # 解析搜索结果
            music_info = self.parser_search(search_result)
            # 生成sign
            sign = self.sign_generator(music_info['mid'])
            data = '{"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch",' \
                   '"param":{"guid":"5478851242","calltype":0,"userip":""}},"req_0":' \
                   '{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":' \
                   '{"guid":"5478851242","songmid":["' + music_info['mid'] + \
                   '"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":' \
                   '{"uin":0,"format":"json","ct":24,"cv":0}}'
            params = {
                'sign': sign,
                'format': 'json',
                'data': data
            }
            # 获取歌曲页数据
            music_result = self.get_page(self.url[1], params)
            # 解析歌曲页得到下载链接
            music_url = self.parser_music(music_result)
            # 下载music
            music = requests.get(music_url, headers=self.headers)
            self.save(music_info, music)
            print('下载完成！')
        except Exception as e:
            print(f'运行出错：{e}，请稍后重试！')


if __name__ == '__main__':
    word = input('请输入歌名：')
    qq = Music_Download(word)
    qq.run()


