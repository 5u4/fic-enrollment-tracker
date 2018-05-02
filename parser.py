from bs4 import BeautifulSoup
import datetime
from config import COURSES, SMTP_RECIPIENTS
from sender import notify

def parse(content):
    soup = BeautifulSoup(content, 'lxml')

    if soup.find('title'):
        print 'refresh your cookies'
        notify(SMTP_RECIPIENTS, "REFRESH COOKIES", "If you receive this email, please check your FIC account and refresh cookies")

    inputs = soup.find_all('input')

    for input in inputs:
        course = input.get('id')
        if course in COURSES and not input.attrs.has_key('disabled'):
            print course, datetime.datetime.now()
            message = "Course " + course + " is available to enroll at " + str(datetime.datetime.now())
            notify(SMTP_RECIPIENTS, "FIC COURSE AVAILABLE!!!", message)
