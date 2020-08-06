import random
import threading
import requests

headers1 = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "cookie":
    "yj0M_5ed6_saltkey=vBhezKzY; yj0M_5ed6_lastvisit=1595763031; yj0M_5ed6_auth=8975ntPpE7hIbg74pSyFJ8b6z2N97TQy85SViB2mMiiw7AGUCyL2MJ8uvOzdJZVEXb8giv1%2B8WHHjjsvLIbymi7pnbI; yj0M_5ed6_lastcheckfeed=934165%7C1595766635; yj0M_5ed6_nofavfid=1; yj0M_5ed6_smile=1D1; yj0M_5ed6_home_diymode=1; yj0M_5ed6_ulastactivity=1596715436%7C0; yj0M_5ed6_sendmail=1; yj0M_5ed6_lastact=1596715436%09home.php%09spacecp; yj0M_5ed6_checkpm=1",
}
url1 = "https://www.soushu.info/home.php?mod=task&do=apply&id=2"
res1 = requests.post(url=url1, headers=headers1).text


def q():
    m = random.randint(0, 255)
    n = random.randint(0, 255)
    x = random.randint(0, 255)
    y = random.randint(0, 255)
    ip = str(m) + "." + str(n) + "." + str(x) + "." + str(y)
    url = 'https://www.soushu.info/forum.php?fromuid=941145'
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
    "yj0M_5ed6_saltkey=vBhezKzY; yj0M_5ed6_lastvisit=1595763031; yj0M_5ed6_auth=8975ntPpE7hIbg74pSyFJ8b6z2N97TQy85SViB2mMiiw7AGUCyL2MJ8uvOzdJZVEXb8giv1%2B8WHHjjsvLIbymi7pnbI; yj0M_5ed6_lastcheckfeed=934165%7C1595766635; yj0M_5ed6_nofavfid=1; yj0M_5ed6_smile=1D1; yj0M_5ed6_home_diymode=1; yj0M_5ed6_ulastactivity=1596715436%7C0; yj0M_5ed6_sendmail=1; yj0M_5ed6_lastact=1596715436%09home.php%09spacecp; yj0M_5ed6_checkpm=1",
}
url3 = "https://www.soushu.info/home.php?mod=task&do=draw&id=2"
res3 = requests.post(url=url3, headers=headers3).text
