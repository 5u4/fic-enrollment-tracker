from bs4 import BeautifulSoup
import datetime
from config import COURSES, SMTP_RECIPIENTS
from sender import notify

emails = []
ENROLLMENT_URL = "https://learning.fraseric.ca/enrolment/units"

def parse(content):
    soup = BeautifulSoup(content, 'lxml')

    if soup.find('title'):
        notify(SMTP_RECIPIENTS, "Refresh Cookies", "If you receive this email, please check your FIC account and refresh cookies")
        exit('Refresh your cookies')

    inputs = soup.find_all('input')

    for input in inputs:
        course = input.get('id')
        if course in COURSES and not input.attrs.has_key('disabled'):
            print course, datetime.datetime.now()
            message = "Course " + course + " is available to enroll at " + str(datetime.datetime.now()) + "\n\n" + ENROLLMENT_URL
            if course not in emails:
                notify(SMTP_RECIPIENTS, "FIC Course Available", message)
                emails.append(course)
