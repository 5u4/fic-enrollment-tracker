from bs4 import BeautifulSoup
from config import COURSES, SMTP_RECIPIENTS
from sender import notify

def parse(content):
    # parse content using beautiful soup
    soup = BeautifulSoup(content, 'lxml')

    # if title found, FIC is requesting login => cookies are expired
    if soup.find('title'):
        notify(SMTP_RECIPIENTS, "Refresh Cookies", "If you receive this email, please check your FIC account and refresh cookies")
        exit('Refresh your cookies')

    # all courses has a input tag which states the course id and the availability
    inputs = soup.find_all('input')
    courses = []

    for input in inputs:
        # get course id
        course = input.get('id')

        # check if is the monitored course and is not disabled
        if course in COURSES and not input.attrs.has_key('disabled'):
            courses.append(course)

    return courses
