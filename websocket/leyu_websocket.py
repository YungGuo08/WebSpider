import requests
import websocket
import time

token_url = 'https://www.611.com/Live/GetToken'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}

def get_token():
    return requests.get(token_url, headers=headers, verify=False).json()['Data']


class Leyu:
    def __init__(self):
        self.token = get_token()
        self.wss_url = f'wss://push.611.com:6119/{self.token}'
        self.socket = websocket.WebSocketApp(self.wss_url, on_message=self.on_message,
                                             on_error=self.on_error, on_close=self.on_close,
                                             on_open=self.on_open)

    def login(self):
        msg = '{"command":"RegisterInfo","action":"Web","ids":[],"UserInfo":{"Version":"[' + str(int(time.time())) + '000' + ']{\\"chrome\\":true,\\"version\\":\\"86.0.4240.183\\",\\"webkit\\":true}","Url":"https://live.611.com/zq"}}'
        self.socket.send(msg)

    def join_group(self):
        msg1 = '{"command":"JoinGroup","action":"SoccerLiveOdd","ids":[]}'
        msg2 = '{"command":"JoinGroup","action":"SoccerLive","ids":[]}'
        self.socket.send(msg1)
        self.socket.send(msg2)

    def on_message(self, message):
        print(message)

    def on_error(self, error):
        print('报错:', error)

    def on_close(self):
        pass

    def on_open(self):
        self.login()
        self.join_group()
        print('握手成功！')

    def run(self):
        self.socket.run_forever()


if __name__ == '__main__':
    ly = Leyu()
    ly.run()


