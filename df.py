# -*- coding: utf8 -*-
# -*- coding: utf8 -*-
import requests
import os
import re
import time
from urllib.parse import quote


def start():
    try:
        s = requests.session()
        cookie =  os.environ["COOKIEDF"]
        sckey =  os.environ["SCKEY"]
        this_time = int(round(time.time() * 1000))
        login_url = 'https://touhou.plus/user/checkin'
        headers={
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'accept-encoding':'gzip, deflate, br',
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language':'zh-CN,zh;q=0.9,en;q=0.8',
            'Cookie': cookie
        }
        res =s.post(login_url,headers=headers).text
        print('访问结果：'+res)
    except Exception as e:
        print("地址访问失败，通知SERVER酱！")
        requests.get('https://sc.ftqq.com/'+sckey+'.send?text=' + quote('白嫖V2访问出现问题~'+time.strftime('%Y.%m.%d',time.localtime(time.time()))) +'&desp='+quote('异常代码：\n'+str(e)))
def main_handler(event, context):
    return start()
if __name__ == '__main__':
    start()
