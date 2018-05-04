import requests
from config import COOKIE, HEADERS, SMTP_RECIPIENTS
from sender import notify

def request(url):
    response = requests.get(url, cookies=COOKIE, headers=HEADERS)

    if response.status_code == 200:
        return response
    else:
        notify(SMTP_RECIPIENTS, "Wrong Response From Server", response.content)
        exit('Wrong response from server')
