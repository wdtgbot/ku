import time

import requests
import os


def q():
    url = 'https://www.93hsy.com/plugin.php?id=it618_award:ajax&ac=getaward&formhash=a7cfe854&_=' + str(
        int(time.time()))
    url1 = 'https://www.93hsy.com/plugin.php?id=it618_award:ajax&formhash=a7cfe854&ac=getcredits'
    cookie = os.environ["COOKIEHS"]
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'cookie': cookie
    }
    res = requests.get(url=url, headers=headers).text
    res1 = requests.get(url=url1, headers=headers).text
    print(res1)


for i in range(200):
    q()
