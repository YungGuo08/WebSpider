import execjs
import hashlib


"""
说明：
# 请求歌曲需加cookie，其中kg_mid是必须参数！
# 如果发现cookie失效（排除其它原因，那么应该就是cookie中的kg_mid失效了）
# 请调用hash_md5方法生成一个kg_mid。
"""


def random_string():
    """
    生成随机字符串
    :return:
    """
    generate_string = execjs.eval('(((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1)')
    return generate_string


def hash_md5():
    """
    MD5加密
    :return: 返回加密后的字符串
    """
    # 组合随机字符串
    string = random_string() + random_string() + '-' + random_string() + '-' + random_string() + \
             '-' + random_string() + '-' + random_string() + random_string() + random_string()
    hash_ = hashlib.md5()
    hash_.update(string.encode())
    kg_mid = hash_.hexdigest()
    return kg_mid
