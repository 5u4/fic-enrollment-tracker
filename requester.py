import requests
from config import COOKIE, SMTP_RECIPIENTS
from sender import notify

def request(url):
    headers = {
        "Host": "learning.fraseric.ca",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "https://learning.fraseric.ca/enrolment/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    }

    response = requests.get(url, cookies=COOKIE, headers=headers)

    if response.status_code == 200:
        return response
    else:
        notify(SMTP_RECIPIENTS, "Wrong Response From Server", response.content)
        exit('Wrong response from server')
