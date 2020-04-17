#Test Script for SOC Challenge for 422
#Version 1.0

import time as t
import requests
import random as random
from datetime import datetime
from socket import *

print("#####################" + "\r")
print("Ready for a Challenge" + "\r")
print("#####################" + "\r")

#Set Payload
payload = "WelcomeToTheSocChallenge"

#set the Destination IP
uri = "3.94.231.16"

#Set Request Headers
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.40 Safari/537.36',
                          'referer': 'http://www.twitter.com'}
#Web Traffic Loop
time = datetime.now()
time = time.strftime("%d/%m/%Y %H:%M:%S")

print("Web Loop Start: " + time)

count = 1
while count < 5:
    t.sleep(random.randint(1,3))
    links=['http://www.google.com','http://www.twitter.com', 'http://' + uri, 'http://www.espn.com', 'http://www.reddit.com',
     'http://www.github.com', 'http://www.yahoo.com', 'http://www.etrade.com', 'http://www.cnn.com']

    for url in links:
            r = requests.get(url,headers=HEADERS,data=payload)
            t.sleep(random.randint(1,3))
    count = count+1
    print("Web Loop Count: ", count)
else:
    time = datetime.now()
    time = time.strftime("%d/%m/%Y %H:%M:%S")
    print("Web Loop End: " + time)

time = datetime.now()
time = time.strftime("%d/%m/%Y %H:%M:%S")

#Port Scan Loop
targetlist = ['192.168.1.1', '192.168.1.2']

for target in targetlist:
    print("Port Scanning: " + target + " at " + time)
    for i in range(50, 55):
         s = socket(AF_INET, SOCK_STREAM)
         conn = s.connect_ex((target, i))
         t.sleep(random.randint(1,3))
         if(conn == 0) :
            print ('Port %d: OPEN ' % (i,))
         s.close()
