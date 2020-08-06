import random
import threading
import requests


def q():
    m = random.randint(0, 255)
    n = random.randint(0, 255)
    x = random.randint(0, 255)
    y = random.randint(0, 255)
    ip = str(m) + "." + str(n) + "." + str(x) + "." + str(y)
    url = 'https://www.soushu.info/forum.php?fromuid=934165'
    headers = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "X-forwarded-for":
        str(ip),
        "Client_ip":
        str(ip),
        "cookie":
        "yj0M_5ed6_lastvisit=1596716650; yj0M_5ed6_lastact=1596720250%09forum.php%09; yj0M_5ed6_promotion=934165"
    }
    requests.get(url=url, headers=headers).text


for i in range(1):
    t = threading.Thread(target=q)
    t.start()
