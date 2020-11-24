import re
import execjs
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 关闭ssl验证提示
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}
url = 'https://www.yidaiyilu.gov.cn/xwzx/gnxw/87373.htm'


def get_page():
    response = requests.get(url, headers=headers, verify=False)
    return response


def get_parameter(response):
    # 获取cookie参数jsluid
    jsluid = response.headers.get('set-cookie').split(';')[0]
    # 提取js代码
    js_clearance = re.findall('cookie=(.*?);location.href=', response.text)[0]
    # 执行后获得cookie参数js_clearance
    result = execjs.eval(js_clearance).split(';')[0]
    global headers
    headers.update({'cookie': jsluid + '; ' + result})
    response = get_page()
    # 提取参数并转字典
    parameter = json.loads(re.findall(r'};go\((.*?)\)</script>', response.text)[0])
    js_file = ''
    # 判断cookie生成方式
    if parameter['ha'] == 'sha1':
        js_file = 'sha1.js'
    elif parameter['ha'] == 'sha256':
        js_file = 'sha256.js'
    elif parameter['ha'] == 'md5':
        js_file = 'md5.js'
    return parameter, js_file, jsluid


def get_cookie(param, file):
    parameter = {
        "bts": param['bts'],
        "chars": param['chars'],
        "ct": param['ct'],
        "ha": param['ha'],
        "tn": param['tn'],
        "vt": param['vt'],
        "wt": param['wt']
    }
    with open(file, 'r') as f:
        js = f.read()
    cmp = execjs.compile(js)
    # 执行js代码传入参数
    clearance = cmp.call('go', parameter)
    return clearance


def run():
    response = get_page()
    parameter, js_file, jsluid = get_parameter(response)
    clearance = get_cookie(parameter, js_file)
    global headers
    headers.update({'cookie': jsluid + '; ' + clearance})
    html = requests.get(url, headers=headers, verify=False)
    print(html.content.decode())


run()
