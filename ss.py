import random
import threading
import requests

headers1 = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "cookie":
    "yj0M_ae15_saltkey=n0ApaVFI; yj0M_ae15_lastvisit=1596979844; yj0M_ae15_ulastactivity=1597046078%7C0; yj0M_ae15_auth=659bo6fiKjfjYErypokCyV6mSSVv3USE123GmzmMVlD0a1sCkusWOJQc%2Bm0mjLS%2B0pWLQFdC4RAmFplTGu224ozMq9E; yj0M_ae15_lastcheckfeed=934165%7C1597046078; yj0M_ae15_lip=13.78.14.245%2C1597046078; yj0M_ae15_nofavfid=1; yj0M_ae15_noticeTitle=1; yj0M_ae15_sendmail=1; yj0M_ae15_lastact=1597046430%09misc.php%09patch",
}
url1 = "https://bbs.kansoushu.com/home.php?mod=task&do=apply&id=2"
res1 = requests.post(url=url1, headers=headers1).text


def q():
    m = random.randint(0, 255)
    n = random.randint(0, 255)
    x = random.randint(0, 255)
    y = random.randint(0, 255)
    ip = str(m) + "." + str(n) + "." + str(x) + "." + str(y)
    url = 'https://bbs.kansoushu.com/forum.php?fromuid=934165'
    headers = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "X-forwarded-for":
        str(ip),
        "Client_ip":
        str(ip),
        "cookie":
        "yj0M_5ed6_saltkey=rx9ucDZ0; yj0M_5ed6_lastvisit=1596710921; yj0M_5ed6_promotion=941145; yj0M_5ed6_lastact=1596714523%09home.php%09misc; yj0M_5ed6_sendmail=1"
    }
    requests.get(url=url, headers=headers).text


for i in range(100):
    t = threading.Thread(target=q)
    t.start()

headers3 = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "cookie":
    "yj0M_ae15_saltkey=n0ApaVFI; yj0M_ae15_lastvisit=1596979844; yj0M_ae15_ulastactivity=1597046078%7C0; yj0M_ae15_auth=659bo6fiKjfjYErypokCyV6mSSVv3USE123GmzmMVlD0a1sCkusWOJQc%2Bm0mjLS%2B0pWLQFdC4RAmFplTGu224ozMq9E; yj0M_ae15_lastcheckfeed=934165%7C1597046078; yj0M_ae15_lip=13.78.14.245%2C1597046078; yj0M_ae15_nofavfid=1; yj0M_ae15_noticeTitle=1; yj0M_ae15_sendmail=1; yj0M_ae15_lastact=1597046430%09misc.php%09patch",
}
url3 = "https://www.soushu.info/home.php?mod=task&do=draw&id=2"
res3 = requests.post(url=url3, headers=headers3).text
