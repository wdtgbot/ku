import requests

cookie = "s_gkr8_f779_saltkey=d92JzEEz; s_gkr8_f779_lastvisit=1597041449; s_gkr8_f779_auth=a865OfIZJUwILqdlDNKa44rd1n0EgBzea2zsUWGEx4zvPhwOGpCu5n9vm2NI04RlQ5BLdmUgMj55D7oeEgKfRW4c1eoG; s_gkr8_f779_ulastactivity=fbd5gC6E0io9VINGewrSrKd3Lk6HFnrAM7Hp4P%2F9oksHcXiatPGe; s_gkr8_f779_connect_is_bind=0; s_gkr8_f779_forum_lastvisit=D_4_1597045075; s_gkr8_f779_visitedfid=4D116; s_gkr8_f779_smile=4D1; s_gkr8_f779_sid=044E55; s_gkr8_f779_lastact=1597045485%09home.php%09misc; s_gkr8_f779_sendmail=1"
url = "https://www.tsdm39.net/plugin.php?id=np_cliworkdz:work"
data1 = {"act": "clickad"}
data2 = {"act": "getcre"}


def q():
    headers = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "cookie": cookie,
        "Referer": "https://www.tsdm39.net/plugin.php?id=np_cliworkdz:work",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": 'application/x-www-form-urlencoded'
    }
    for i in range(6):
        res1 = requests.post(url=url, headers=headers, data=data1).text
    for i in range(1):
        res2 = requests.post(url=url, headers=headers, data=data2).text


def main_handler(event, context):
    return q()


if __name__ == "__main__":
    q()
