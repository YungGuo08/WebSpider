import requests
import csv
import emoji
import re
import time
import datetime
from QQ_Music.Setting import SAVE_ADDRESS, PAGE_NUM, PAGE_SIZE, CMD, SPECIAL_SYMBOLS_LIST


class Music_Comment(object):

    def __init__(self, keyword):
        # 搜索接口/歌曲页接口/评论接口
        self.url = ['https://c.y.qq.com/soso/fcgi-bin/client_search_cp?',
                    'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?']
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
        self.ok_count = 0

    def save(self, info, name, content, praise_num):
        """
        保存
        :param info: 歌曲信息
        :param name: 用户名
        :param content: 评论内容
        :param praise_num: 点赞数
        :return:
        """
        music_name = info['music_name']
        singer = info['singer']
        with open(f"{SAVE_ADDRESS}{music_name}-{singer}.csv", 'at', encoding='gbk', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name, content, praise_num])

    def get_page(self, url, params):
        """
        请求页面
        :param url: 请求url
        :param params: 传递参数
        :return:
        """
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def filter_symbol(self, content):
        """
        过滤emoji表情/特殊符号
        :param content: 返回过滤后的内容
        :return:
        """
        # 过滤特殊符号
        for special_symbols in SPECIAL_SYMBOLS_LIST:
            if special_symbols in content:
                content = content.replace(special_symbols, '')
        # 过滤emoji表情
        content = re.sub(r'(:.*?:)', '', emoji.demojize(content))
        return content

    def parser_comment(self, data, info, page):
        """
        解析评论
        :param data: 评论数据
        :return:
        """
        data_list = data['comment']['commentlist']
        print(f'正在保存第{page}页...')
        for data in data_list:
            # 用户名
            nick = data['nick']
            nick = self.filter_symbol(nick)
            try:
                # 评论内容
                if data['middlecommentcontent'] is None:
                    content = data['rootcommentcontent'].strip().replace('\n', '')
                    content = self.filter_symbol(content)
                else:
                    reply_nick = data['middlecommentcontent'][0]['replyednick']
                    reply_nick = self.filter_symbol(reply_nick)
                    reply_content = data['middlecommentcontent'][0]['subcommentcontent'].strip().replace('\n', '')
                    content = self.filter_symbol(reply_content)
                    content = f'回复{reply_nick}：{content}'
                # 点赞数
                praise_num = data['praisenum']
                # 保存
                self.save(info, nick, content, praise_num)
                self.ok_count += 1
            except Exception as e:
                # 内容报错日志
                with open('content_error.log', 'at') as f:
                    content_error_time = datetime.datetime.now()
                    f.write(f'[{content_error_time}]: {e}\n')

    def parser_search(self, data):
        """
        解析搜索页
        :param data: 搜索页数据
        :return: 返回歌曲信息
        """
        music_info = {}
        data = data['data']['song']['list'][0]
        # 歌曲mid、歌名、歌手、id
        music_info['mid'] = data['mid']
        music_info['music_name'] = data['name']
        music_info['singer'] = data['singer'][0]['name']
        music_info['id'] = data['id']
        return music_info

    def run(self):
        try:
            # 获取搜索页数据
            search_result = self.get_page(self.url[0], self.params)
            # 解析搜索结果
            music_info = self.parser_search(search_result)
            run_time = time.time()
            # 评论计数
            comment_count = 0
            for page in range(0, PAGE_NUM):
                params = {
                    'reqtype': 2,
                    'biztype': 1,
                    'topid': music_info['id'],
                    'cmd': CMD,
                    'pagenum': page,
                    'pagesize': PAGE_SIZE
                }
                comment_result = self.get_page(self.url[1], params)
                # 解析评论
                self.parser_comment(comment_result, music_info, page)
                comment_count += PAGE_SIZE
            end_time = time.time()
            print('-' * 50)
            print(f'保存完成：本次共保存{self.ok_count}条评论，{comment_count - self.ok_count}条评论未保存，'
                  f'用时：{int(end_time - run_time)}秒')
        except Exception as e:
            print(f'运行出错：{e}，请稍后重试！')


if __name__ == '__main__':
    word = input('请输入歌名：')
    qq = Music_Comment(word)
    qq.run()
