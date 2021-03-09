
import requests
import os

cookie =  os.environ["COOKIECH"]
formhash =  os.environ["FORMHASHCH"]
def q():
    url = 'https://www.cunhua.casa/k_misign-sign.html?operation=qiandao&format=global_usernav_extra&formhash='+str(formhash)+'&inajax=1&ajaxtarget=k_misign_topb'
    headers = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "cookie": cookie,
    }
    res = requests.post(url=url, headers=headers).text
    print(res)


def main_handler(event, context):
    return q()


if __name__ == "__main__":
    q()
