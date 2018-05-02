from requester import request
from parser import parse
import time, datetime
from config import URLS

counter = 0

while True:
    print "Start " + str(counter) + " search " + str(datetime.datetime.now()) + "\n"
    for url in URLS:
        response = request(url)
        parse(response.content)
    counter += 1
    print "Search Done\n"
    time.sleep(60)
