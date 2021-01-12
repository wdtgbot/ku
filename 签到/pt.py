import requests
import os

cookie = os.environ["COOKIEPT"]
def q():
    url = 'https://pthome.net/attendance.php'
    headers = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "cookie": cookie,
    }
    res = requests.post(url=url, headers=headers).text
    print(res)


def main_handler(event, context):
    return q()


if __name__ == "__main__":
    q()
