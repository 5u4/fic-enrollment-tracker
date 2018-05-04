from requester import request
from parser import parse
import time, datetime
from config import URLS, FREQUENCY

counter = 0

while True:
    print "Start " + str(counter) + " search " + str(datetime.datetime.now())
    for url in URLS:
        response = request(url)
        parse(response.content)
    counter += 1
    print "Search Done"
    time.sleep(FREQUENCY)
