import re

import requests


def q():
    url1 = 'https://bbs.fygal.com/kf_fw_ig_index.php'
    cookie = '2ed4e_skinco=default; 2ed4e_ck_info=%2F%09; 2ed4e_winduser=BQwLBAQDO1INUlJQAQIKVwYAAVpSDgFTAVEEBQMDVFcPAQAGBgFQPw%3D%3D; Hm_lvt_f83dc734066b108cb0068c6118d230ce=1596612607; 2ed4e_ipfrom=d2fc22a30630299f28d9b24b06e33649%09%C3%C0%B9%FA%0D; PHPSESSID=ha2khca87kvvpna2nt9qll1604; 2ed4e_ol_offset=17266; 2ed4e_lastpos=other; 658221_pd_changePointsInfo=6c; 2ed4e_lastvisit=2659%091597044316%09%2Fkf_fw_ig_index.php%3F'
    headers = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "cookie": cookie,
    }
    res1 = requests.post(url=url1, headers=headers).text
    a = re.findall(r'data: "safeid=(.+?)"', res1, re.S)
    a = a[-1]
    url3 = 'https://bbs.fygal.com/kf_fw_ig_halo.php?do=buy&id=2&safeid=' + str(a)
    res3 = requests.get(url=url3, headers=headers).text


def main_handler(event, context):
    return q()


if __name__ == "__main__":
    q()
