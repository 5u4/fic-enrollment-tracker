import requests
from config import COOKIE, HEADERS, COMMA_ASCII, ENROLLMENT_URL

def enroll(courses):
    # build course params
    params = "choice%5BU2HA%5D=" + COMMA_ASCII.join(courses) + "&submit.x=102&submit.y=23"

    # enroll
    return requests.post(ENROLLMENT_URL, params=params, headers=HEADERS, cookies=COOKIE)
