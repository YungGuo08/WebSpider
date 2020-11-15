import asyncio
import requests
import logging
import time
from aiowebsocket.converses import AioWebSocket


def get_token():
    url = 'https://www.611.com/Live/GetToken'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    return requests.get(url, headers=headers, verify=False).json()['Data']


async def startup(uri):
    async with AioWebSocket(uri) as aws:
        converse = aws.manipulator
        # 向服务器发送消息
        await converse.send('{"command":"RegisterInfo","action":"Web","ids":[],"UserInfo":{"Version":"[' + str(int(time.time())) + '000' + ']{\\"chrome\\":true,\\"version\\":\\"86.0.4240.183\\",\\"webkit\\":true}","Url":"https://live.611.com/zq"}}')
        await converse.send('{"command":"JoinGroup","action":"SoccerLiveOdd","ids":[]}')
        await converse.send('{"command":"JoinGroup","action":"SoccerLive","ids":[]}')
        while True:
            mes = await converse.receive()
            print(mes)


if __name__ == '__main__':
    token = get_token()
    remote = f'wss://push.611.com:6119/{token}'
    try:
        asyncio.get_event_loop().run_until_complete(startup(remote))
    except KeyboardInterrupt as exc:
        logging.info('Quit.')
