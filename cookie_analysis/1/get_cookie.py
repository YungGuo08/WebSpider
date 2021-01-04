import re
import execjs
import requests
import json
from requests.utils import add_dict_to_cookiejar
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 关闭ssl验证提示
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
}
url = 'https://www.yidaiyilu.gov.cn/xwzx/gnxw/87373.htm'
# 使用session保持会话
session = requests.session()


def get_parameter(response):
    # 提取js代码
    js_clearance = re.findall('cookie=(.*?);location', response.text)[0]
    # 执行后获得cookie参数js_clearance
    result = execjs.eval(js_clearance).split(';')[0].split('=')[1]
    # 添加cookie
    add_dict_to_cookiejar(session.cookies, {'__jsl_clearance_s': result})
    # 第二次请求
    response = session.get(url, headers=header, verify=False)
    # 提取参数并转字典
    parameter = json.loads(re.findall(r';go\((.*?)\)', response.text)[0])
    js_file = ''
    # 判断加密方式
    if parameter['ha'] == 'sha1':
        js_file = 'sha1.js'
    elif parameter['ha'] == 'sha256':
        js_file = 'sha256.js'
    elif parameter['ha'] == 'md5':
        js_file = 'md5.js'
    return parameter, js_file


def get_cookie(param, file):
    with open(file, 'r') as f:
        js = f.read()
    cmp = execjs.compile(js)
    # 执行js代码传入参数
    clearance = cmp.call('go', param)
    return clearance


def run():
    # 第一次请求
    response = session.get(url, headers=header, verify=False)
    # 获取参数及加密方式
    parameter, js_file = get_parameter(response)
    # 获取cookie
    clearance = get_cookie(parameter, js_file)
    # 修改cookie
    add_dict_to_cookiejar(session.cookies, {'__jsl_clearance_s': clearance})
    # 第三次请求
    html = session.get(url, headers=header, verify=False)
    print(html.content.decode())


run()
