"""
参数说明：
SAVE_ADDRESS：下载歌曲/评论保存地址，默认为当前目录（./）；可自行更改，注意将目录结构中的‘\’改为‘/’
PAGE_NUMBER：页数，默认值为1；如果修改此参数，数值不要超过实际评论页数，并且需要将评论数的值固定为20
COMMENT_NUMBER：评论数，默认值为20；如果修改此参数，数值不能超过1000，并且需要将页数的值固定为1
COMMENT_TYPE：评论类型，默认值为0；【0】所有评论【1】精彩评论（每首歌的精彩评论只有15条）

具体三种保存方式：
一、保存所有评论
1、将PAGE_NUMBER设为实际评论页数（网易云音乐上的评论页数），或者根据自己需要设置页数（不要超过实际页数）；
2、将COMMENT_NUMBER设为20；
3、将COMMENT_TYPE设为0。

二、保存1000条评论：
1、将PAGE_NUMBER设为1；
2、将COMMENT_NUMBER设为1000；
3、将COMMENT_TYPE设为0。

三、保存精彩评论
1、将PAGE_NUMBER设为1；
2、将COMMENT_NUMBER设为20；
3、将COMMENT_TYPE设为1。

ps：务必根据要求设置，设置错误可能会导致获取不到数据或者数据错乱。
"""

# 保存地址，默认当前目录
SAVE_ADDRESS = './'

# 页数，例如改为10，将会保存第1页到第10页的评论（共200）
PAGE_NUMBER = 1

# 评论数
COMMENT_NUMBER = 20

# 评论类型
COMMENT_TYPE = 0

"""
说明：如果觉得少一些评论不影响，那就不用管下面的设置，这个是对特殊符号过滤用的
因为评论中包含特殊符号无法保存到csv文件中；
将目录下的content_error.log文件中提示的编码加入到下面的列表中，
并删除上一次保存的数据重新开始（不删除会导致数据重复），再重新运行程序。
目前能力有限，只能暂时用此方法解决特殊符号的问题
"""
# 特殊符号列表
SPECIAL_SYMBOLS_LIST = ['\u200b', '\u22ef', '\u0e07', '\u2661', '\u2022',
                        '\u0300', '\u0301', '\u0a87', '\u2741', '\u272a',
                        '\xa0', '\ufffc', '\u2006', '\u2039', '\xb4', '\u30fb',
                        '\u2212', '\u0942', '\uff65', '\u2449', '\u22c6',
                        '\u0e51', '\u0ac5', '\u1dc4', '\u263e']

"""
加密固定参数，不要修改
"""
# 固定key
KEY = '0CoJUm6Qyw8W8jud'

# 固定值参数
FIXED_VALUE = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7' \
              'b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280' \
              '104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932' \
              '575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b' \
              '3ece0462db0a22b8e7'

# 偏移量参数
IV = '0102030405060708'

# headers请求头
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
    'content-type': 'application/x-www-form-urlencoded'
}


