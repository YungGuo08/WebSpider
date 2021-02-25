import random
import requests
import csv
import re
import emoji
import time
import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from Encryption import AES_Encrypt, Encrypt_String, Random_String
from Setting import SAVE_ADDRESS, PAGE_NUMBER, COMMENT_NUMBER, \
    COMMENT_TYPE, SPECIAL_SYMBOLS_LIST, KEY, FIXED_VALUE, IV, HEADERS

# 关闭ssl验证错误提醒
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Music_Comment(object):

    def __init__(self, keyword):
        # 加密固定key参数
        self.key = KEY
        # 加密固定值参数
        self.fixed_value = FIXED_VALUE
        # 加密偏移量参数
        self.iv = IV
        # 关键参数（需要加密的字符串）
        self.key_parameter = r'{"hlpretag":"<span class=\"s-fc7\">","hlposttag":"</span>","s":"' + keyword + \
                             r'","type":"1","offset":"0","total":"true","limit":"30","csrf_token":""}'
        # 搜索页接口、评论页接口
        self.url = ['https://music.163.com/weapi/cloudsearch/get/web?csrf_token=',
                    'https://music.163.com/weapi/comment/resource/comments/get?csrf_token=']
        self.headers = HEADERS
        # 评论翻页关键参数，初始值为-1
        self.cursor = -1

    def encrypt(self):
        """
        加密params/encSecKey
        :return: data
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

    def save(self, music_name, user_name, content, liked_count):
        """
        保存
        :param music_name: 歌曲名
        :param user_name: 用户名
        :param content: 评论内容
        :return:
        """
        with open(f'{SAVE_ADDRESS}{music_name}.csv', 'at', encoding='gbk', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([user_name, content, liked_count])

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
        select = int(input('请输入对应数字选择歌曲：'))
        result = {}
        # id
        result['id'] = data['songs'][select]['id']
        # 歌名
        result['music_name'] = data['songs'][select]['name']
        # 歌手名
        result['singer'] = data['songs'][select]['ar'][0]['name']
        return result

    def parser_comment(self, music_id, music_name):
        """
        解析评论数据
        :param music_id: 歌曲id
        :param music_name: 歌曲名
        :return:
        """
        run_time = time.time()
        # 保存成功计数/评论计数
        ok_count = 0
        comment_count = 0
        for page_no in range(1, PAGE_NUMBER + 1):
            try:
                # 评论页关键参数
                self.key_parameter = r'{"rid":"R_SO_4_' + str(music_id) + '","threadId":"R_SO_4_' + str(music_id) + \
                                     '","pageNo":"' + str(page_no) + '","pageSize":"' + str(COMMENT_NUMBER) + \
                                     '","cursor":"' + str(self.cursor) + '","offset":"0","orderType":"1","csrf_token":""}'
                # 获取评论数据
                comment_data = self.post_page(self.url[1], self.encrypt())['data']
                self.cursor = comment_data['cursor']
                comment_list = None
                if COMMENT_TYPE == 0:
                    comment_list = comment_data['comments']
                    print(f'正在保存第{page_no}页评论...')
                elif COMMENT_TYPE == 1:
                    comment_list = comment_data['hotComments']
                    print('正在保存精彩评论...')
                else:
                    print('参数错误！')
                for comment in comment_list:
                    # 用户名
                    name = comment['user']['nickname']
                    try:
                        # 评论内容
                        content = comment['content'].strip().replace('\n', '')
                        # 过滤特殊符号
                        for special_symbols in SPECIAL_SYMBOLS_LIST:
                            if special_symbols in content:
                                content = content.replace(special_symbols, '')
                        # 过滤emoji表情
                        content = re.sub(r'(:.*?:)', '', emoji.demojize(content))
                        # 点赞数
                        liked_count = comment['likedCount']
                        self.save(music_name, name, content, liked_count)
                        ok_count += 1
                    except Exception as e:
                        # 内容报错日志
                        with open('content_error.log', 'at') as f:
                            content_error_time = datetime.datetime.now()
                            f.write(f'[{content_error_time}]: {e}\n')
            except:
                print(f'>>>第{page_no}页数据获取失败！')
            comment_count += 20
        end_time = time.time()
        print('-' * 50)
        # print(f'保存完成：本次共保存{ok_count}条评论，{comment_count - ok_count}条评论未保存，用时：{int(end_time - run_time)}秒')
        print(f'保存完成：本次共保存{ok_count}条评论，用时：{int(end_time - run_time)}秒')


if __name__ == '__main__':
    try:
        key_word = input('请输入歌名：')
        music = Music_Comment(key_word)
        # 获取搜索结果
        result_info = music.parser_search()
        # 解析评论数据
        music.parser_comment(result_info['id'], result_info['music_name'])
    except:
        print('未获取到搜索页数据，请稍后重新运行！')
