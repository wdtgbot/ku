import re

import requests

import os

cookie = os.environ["COOKIEFY"]
def q():
    url1 = 'https://bbs.365gal.com/kf_fw_ig_index.php'
    headers = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
        "cookie": cookie,
    }
    res1 = requests.post(url=url1, headers=headers).text
    a = re.findall(r'data: "safeid=(.+?)"', res1, re.S)
    a = a[-1]
    url3 = 'https://bbs.365gal.com/kf_fw_ig_halo.php?do=buy&id=2&safeid=' + str(a)
    res3 = requests.get(url=url3, headers=headers).text


def main_handler(event, context):
    return q()


if __name__ == "__main__":
    q()
