# Mail Sending
SMTP_USER = "email@example.com"
SMTP_PWD = "password"
SMTP_RECIPIENTS=["email@example.com"]

# FIC Credentials
COOKIES = {
    "__utma": "",
    "__utmz": "",
    "NVT": ""
}

# FIC Request Headers
HEADERS = {
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

# Courses Need To Be Tracked
COURSES = []

# Courses Fetching Url
URLS = []

# Gap Time Between Two Searches (in Seconds)
FREQUENCY = 30

# ----------------------- App Constants (Do NOT Change Unless You Know What You Doing) -----------------------

ENROLLMENT_URL = "https://learning.fraseric.ca/enrolment/confirmation"
COMMA_ASCII = "%2C"

ENROLLMENT_PAGE = "https://learning.fraseric.ca/enrolment/units"
