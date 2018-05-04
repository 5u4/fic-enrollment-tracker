from requester import request
from parser import parse
import time, datetime
from config import URLS, FREQUENCY, SMTP_RECIPIENTS, ENROLLMENT_PAGE
from sender import notify

counter = 0

while True:
    # clear email sending list every 10 iterations
    if counter % 10 == 0:
        emails = []

    # start searching
    print "Start " + str(counter) + " search " + str(datetime.datetime.now())

    # fetch information from each url
    for url in URLS:
        response = request(url)
        courses = parse(response.content)

        # notify user when courses are available
        for course in courses:
            if course not in emails:
                message = "Course " + course + " is available to enroll at " + \
                          str(datetime.datetime.now()) + "\n\n" + ENROLLMENT_PAGE
                notify(SMTP_RECIPIENTS, "FIC Course Available", message)
                emails.append(course)

    # finish search
    print "Search Done"
    counter += 1

    # wait for a period
    time.sleep(FREQUENCY)
