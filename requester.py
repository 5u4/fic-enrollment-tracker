import requests
from config import COOKIE, SMTP_RECIPIENTS
from sender import notify

def request(url):
    response = requests.get(url, cookies=COOKIE)

    if response.status_code == 200:
        return response
    else:
        notify(SMTP_RECIPIENTS, "REFRESH COOKIES", "Please check your FIC account and refresh cookies")
        exit('does not work')
