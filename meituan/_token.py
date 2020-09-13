# @Author: Yun
# @Time  : 2020/9/13 17:12

import base64
import zlib


def encode_token(data):
    """
    将字符串数据转为token
    :param data: 字符串数据
    :return: 返回token
    """
    # 二进制编码
    encode = str(data).encode()
    # 二进制压缩
    compress = zlib.compress(encode)
    # base64编码
    base64_encode = base64.b64encode(compress)
    # 转为字符串
    token_ = str(base64_encode, encoding='utf-8')
    return token_


def decode_token(data):
    """
    将token字符串（base64）解码
    :param data: token字符串
    :return:
    """
    # base64解码
    decode = base64.b64decode(data.encode())
    # 二进制解压
    token_string = zlib.decompress(decode)
    return token_string
