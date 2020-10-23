import base64
import binascii
import random
import string
from Cryptodome.Cipher import AES


def AES_Encrypt(key, iv, data):
    """
    AES加密（CBC模式加密）
    :param key: 密钥
    :param iv: 密斯偏移量
    :param data: 需要加密的字符串
    :return: 返回加密后的字符串
    """
    # 字符串长度
    num = len(data.encode())
    # 字符串补位
    pad = lambda d: d + (16 - num % 16) * chr(16 - num % 16)
    data = pad(data)
    # 加密后得到bytes类型的数据
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    encrypted_bytes = cipher.encrypt(data.encode('utf-8'))
    # 使用Base64进行编码,返回byte字符串
    encode_str = base64.b64encode(encrypted_bytes)
    # 对byte字符串按utf-8进行解码
    text = encode_str.decode()
    return text


def Encrypt_String(fixed_value, random_str):
    """
    加密字符串
    :param fixed_value: 固定值参数
    :param random_str: 随机key
    :return: 返回加密后的字符串
    """
    # 将随机key反转后转成bytes类型数据，再用十六进制表示
    random_str = int(binascii.hexlify(random_str[::-1].encode('utf-8')), 16)
    # pow函数：随机字符串的65537次幂，除以十六进制的固定值参数，再取余
    # hex函数：将pow返回的结果（十进制）转十六进制
    # 最后转为字符串去除hex函数返回结果开头的0x，得到一个字符串
    return str(hex(pow(random_str, 65537, int(fixed_value, 16))))[2:]


def Random_String():
    """
    生成随机key，用于加密
    :return:
    """
    # 生成16位大小写数字组合的字符串
    random_key = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    return random_key
