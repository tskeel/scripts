#Random Traffic Simulator
#Version 1.0
#Author @SecureTacticsTS
#Purpose: This is a simple script to simulate web traffic and perform port scanning.  You can use the sleep variables to varry the time between requests.  

import time as t
import requests
import random as random
from datetime import datetime
from socket import *

print("#################" + "\r")
print("Traffic Sumulator" + "\r")
print("################" + "\r")

#Set Payload
payload = "WelcomeToTheSocChallenge"

#set a specific IP
uri = "18.214.153.235"

#Set sleep min/max in seconds
sleep1 = 1
sleep2 = 2

#Set Web Loop Count
max = 2

#Set Port Scan range
range1 = 50
range2 = 53

#Set Request Headers
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.40 Safari/537.36',
                          'referer': 'http://www.twitter.com'}

#Web Traffic Loop
time = datetime.now()
time = time.strftime("%d/%m/%Y %H:%M:%S")

print("Web Loop Start: " + time)

count = 1
while count < max:
    t.sleep(random.randint(sleep1,sleep2))
    links=['http://www.google.com','http://www.twitter.com', 'http://' + uri, 'http://www.espn.com', 'http://www.reddit.com',
     'http://www.github.com', 'http://www.yahoo.com', 'http://www.etrade.com', 'http://www.cnn.com']

    for url in links:
            r = requests.get(url,headers=HEADERS,data=payload)
            t.sleep(random.randint(sleep1,sleep2))
    count = count+1

else:
    time = datetime.now()
    time = time.strftime("%d/%m/%Y %H:%M:%S")
    print("Web Loop End: " + time)

#Port Scan Loop
targetlist = ['192.168.1.1', '192.168.1.2']

for target in targetlist:
    t.sleep(random.randint(sleep1,sleep2))
    time = datetime.now()
    time = time.strftime("%d/%m/%Y %H:%M:%S")
    print("Port Scanning: " + target + " at " + time)

    for i in range(range1, range2):
         s = socket(AF_INET, SOCK_STREAM)
         conn = s.connect_ex((target, i))
         t.sleep(random.randint(sleep1,sleep2))
         if(conn == 0) :
            print ('Port %d: OPEN ' % (i,))
         s.close()

print("Port Scan Complete")
print("Traffic Simulator Finished")
