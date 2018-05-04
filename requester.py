import requests
from config import COOKIES, HEADERS, SMTP_RECIPIENTS
from sender import notify

def request(url):
    response = requests.get(url, cookies=COOKIES, headers=HEADERS)

    if response.status_code == 200:
        return response
    else:
        notify(SMTP_RECIPIENTS, "Wrong Response From Server", response.content)
        exit('Wrong response from server')
