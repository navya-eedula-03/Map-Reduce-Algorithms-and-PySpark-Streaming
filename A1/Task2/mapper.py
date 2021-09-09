#!/usr/bin/env python
"""mapper.py"""
from datetime import datetime
import math
import sys
import json
import requests
l=[]
url = "http://20.185.44.219:5000/"
headers = {
  'Content-Type': 'application/json'
}

la=sys.argv[1]
lo=sys.argv[2]
d=sys.argv[3]
fixed=(float(la),float(lo))
def dist(a,b):
	t1=(b[0]-a[0])**2
	t2=(b[1]-a[1])**2
	return (t1+t2)**0.5
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    #print(line)
    
    line = line.strip()
    y=json.loads(line)
    if(dist(fixed,(float(y['Start_Lat']),float(y['Start_Lng']))) < float(d)):
    	payload = json.dumps({"latitude":y['Start_Lat'],"longitude":y['Start_Lng']})
    	response = requests.request("POST", url, headers=headers, data=payload)
    	data=response.json()
    	print(data['state'],":",data['city'])