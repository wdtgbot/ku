import random
import threading
import requests
import os

cookie = os.environ["COOKIEHS"]
headers1 = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    "cookie":cookie
}
url1 = "https://www.93hsy.com/home.php?mod=task&do=apply&id=14"
url2 = "https://www.93hsy.com/home.php?mod=task&do=apply&id=15"
url3 = "https://www.93hsy.com/home.php?mod=task&do=apply&id=16"
res1 = requests.post(url=url1, headers=headers1).text
res2 = requests.post(url=url2, headers=headers1).text
res3 = requests.post(url=url3, headers=headers1).text


def q():
    m = random.randint(0, 255)
    n = random.randint(0, 255)
    x = random.randint(0, 255)
    y = random.randint(0, 255)
    ip = str(m) + "." + str(n) + "." + str(x) + "." + str(y)
    url = 'https://www.93hsy.com/?fromuid=619687'
    headers = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
        "X-forwarded-for":
        str(ip),
        "Client_ip":
        str(ip),
        "cookie":
        "yj0M_5ed6_saltkey=rx9ucDZ0; yj0M_5ed6_lastvisit=1596710921; yj0M_5ed6_promotion=941145; yj0M_5ed6_lastact=1596714523%09home.php%09misc; yj0M_5ed6_sendmail=1"
    }
    requests.get(url=url, headers=headers).text


for i in range(300):
    t = threading.Thread(target=q)
    t.start()

headers3 = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "cookie":cookie
}
url4 = "https://www.93hsy.com/home.php?mod=task&do=draw&id=14"
url5 = "https://www.93hsy.com/home.php?mod=task&do=draw&id=15"
url6 = "https://www.93hsy.com/home.php?mod=task&do=draw&id=16"
res4 = requests.post(url=url4, headers=headers3).text
res5 = requests.post(url=url5, headers=headers3).text
res6 = requests.post(url=url6, headers=headers3).text
