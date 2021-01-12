import random
import re
import time
import os
import requests
import sys





path=sys.path[0]+r'/村花.txt'
cookie =  os.environ["COOKIECH"]
formhash =  os.environ["FORMHASHCH"]
def q():
    i = ["40", "38", "39", "41", "42", "46", "47", "48", "101"]
    id = random.choice(i)
    url = "https://www.cunhua.lat/forum-" + str(id) + "-" + str(
        random.randint(1, 10)) + ".html"
    headers = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
        "cookie":cookie
    }
    res = requests.get(url=url, headers=headers).text
    c = str(res)
    zz = r'https://cdn.chcdn.xyz/data/attachment/forum/threadcover/.+?/.+?/(.+?).jpg'
    d = re.findall(zz, c, re.S)
    g = str(d[-1])
    print(g)
    url1 = "https://www.cunhua.lat/forum.php?mod=viewthread&tid=" + str(g)
    res2 = requests.get(url=url1, headers=headers).text
    zzz = r'postmessage_.+?>(.+?)<'
    q = re.findall(zzz, res2, re.S)
    s = str(q[-2]).strip()
    print(s)
    url2 = (
        "https://www.cunhua.lat/forum.php?mod=post&action=reply&fid=" +
        str(id) + "&tid=" + str(g) +
        "&extra=&replysubmit=yes&mobile=2&handlekey=fastpost&loc=1&inajax=1")
    headers1 = {
        "user-agent":
        "Mozilla/5.0 (Linux; Android 10; MI 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36",
        "cookie": cookie,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data1 = {
        "posttime": str(int(time.time())),
        "formhash": formhash,
        "usesig": "1",
        "message": str(s),
    }
    res1 = requests.post(url=url2, headers=headers1, data=data1).text
    print(res1)
    with open(path, 'w+') as f:
        f.write(res1)


def main_handler(event, context):
    return q()


if __name__ == "__main__":
    q()
