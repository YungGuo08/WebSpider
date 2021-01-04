import requests
import re
import execjs
import hashlib
import json
from requests.utils import add_dict_to_cookiejar


def getCookie(data):
    chars = len(data['chars'])
    for i in range(chars):
        for j in range(chars):
            encrypt_chars = data['bts'][0] + data['chars'][i] + data['chars'][j] + data['bts'][1]
            ha = None
            if data['ha'] == 'md5':
                ha = hashlib.md5()
            elif data['ha'] == 'sha1':
                ha = hashlib.sha1()
            elif data['ha'] == 'sha256':
                ha = hashlib.sha256()
            ha.update(encrypt_chars.encode())
            result = ha.hexdigest()
            if result == data['ct']:
                return encrypt_chars


url = 'https://www.cnvd.org.cn/flaw/list.htm'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
session = requests.session()
res1 = session.get(url, headers=header)
jsl_clearance_s = re.findall(r'cookie=(.*?);location', res1.text)[0]
jsl_clearance_s = str(execjs.eval(jsl_clearance_s)).split('=')[1].split(';')[0]
# add_dict_to_cookiejar方法添加cookie
add_dict_to_cookiejar(session.cookies, {'__jsl_clearance_s': jsl_clearance_s})
res2 = session.get(url, headers=header)
data = json.loads(re.findall(r';go\((.*?)\)', res2.text)[0])
jsl_clearance_s = getCookie(data)
# 修改cookie
add_dict_to_cookiejar(session.cookies, {'__jsl_clearance_s': jsl_clearance_s})
res3 = session.get(url, headers=header)
print(res3.text)
