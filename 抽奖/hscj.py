import time

import requests
import os

formhash = os.environ["HASHHS"] 
def q():
    url = 'https://www.93hsy.com/plugin.php?id=it618_award:ajax&ac=getaward&formhash='+str(formhash)+ '&_=' + str(
    int(round(time.time() * 1000)))
    url1 = 'https://www.93hsy.com/plugin.php?id=it618_award:ajax&formhash='+str(formhash)+'&ac=getcredits'
    cookie = os.environ["COOKIEHS"]
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'cookie': cookie
    }
    res = requests.get(url=url, headers=headers).text
    res1 = requests.get(url=url1, headers=headers).text
    print(res1)


for i in range(10):
    q()
