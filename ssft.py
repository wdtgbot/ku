import random
import re
import time
from urllib.parse import urlencode

import requests


def q():
    i = ["39", "40", "56", "68", "74", "77"]
    id = random.choice(i)
    url = "https://bbs.kansoushu.com/forum.php?mod=forumdisplay&fid=" + str(
        id) + "&page=" + str(random.randint(1, 20))
    headers = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    res = requests.get(url=url, headers=headers).text
    c = str(res)
    zz = r'<tbody id="normalthread_.+?">(.+?)</tbody>'
    d = str(re.findall(zz, c, re.S))
    zzz = r"id=\"content_(.+?)\""
    f = re.findall(zzz, d, re.S)
    g = random.choice(f)
    url1 = (
        "https://bbs.kansoushu.com/forum.php?mod=post&action=reply&fid=" +
        str(id) + "&tid=" + str(g) +
        "&extra=page%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1"
    )
    cookie1 = "yj0M_ae15_saltkey=n0ApaVFI; yj0M_ae15_lastvisit=1596979844; yj0M_ae15_nofavfid=1; yj0M_ae15_ulastactivity=1597107578%7C0; yj0M_ae15_auth=9b59UEOOK3RBCs7nRgyLdiALGtSadd9UxMW4s%2FFKgVzKfGfdevqdWo9Dq6IujzThw8jfYgLxOjpHRcRYwsIPaYQHfhg; yj0M_ae15_lastcheckfeed=934165%7C1597107578; yj0M_ae15_lip=183.217.116.98%2C1597107578; yj0M_ae15_noticeTitle=1; yj0M_ae15_st_t=934165%7C1597107838%7Ccab0232b14b4248ed253f202fa35d323; yj0M_ae15_forum_lastvisit=D_39_1597107838; yj0M_ae15_st_p=934165%7C1597107841%7Cb0528815456713c7801cf1a325b53e52; yj0M_ae15_viewid=tid_308299; yj0M_ae15_smile=1D1; yj0M_ae15_lastact=1597107852%09forum.php%09ajax"
    headers1 = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "cookie": cookie1,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    replylist = [
        u"感谢楼主分享",
        u"谢谢楼主分享",
        u"楼主发贴辛苦了",
        u"谢谢楼主分享",
        u"感谢楼主的无私分享",
        u"楼主，大恩不言谢了",
        u"感谢感谢分享",
        u"谢谢老板分享",
    ]
    z = random.choice(replylist)
    data1 = {
        "posttime": str(int(time.time())),
        "formhash": "e4f1b32c",
        "usesig": "1",
        "message": z,
    }
    data1 = urlencode(data1, encoding="gb2312")
    res1 = requests.post(url=url1, headers=headers1, data=data1).text
    print(res1)


def main_handler(event, context):
    return q()


if __name__ == "__main__":
    q()
