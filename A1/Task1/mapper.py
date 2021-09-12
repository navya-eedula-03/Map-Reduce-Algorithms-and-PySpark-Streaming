#!/usr/bin/env python
"""mapper.py"""
from datetime import datetime
	
import sys
import json
l=[]

matches = ['lane blocked', 'shoulder blocked', 'overturned vehicle']
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    
    line = line.strip()
    y=json.loads(line)
    	
    if (y['Severity']>=2 and y['Sunrise_Sunset']=='Night' and y['Visibility(mi)']<= 10 and y['Precipitation(in)']>= 0.2):
    	if(y['Weather_Condition'] in ['Heavy Snow', 'Thunderstorm', 'Heavy Rain', 'Heavy Rain Showers','Blowing Dust']):
    		if any(x in y['Description'].lower() for x in matches):
    			l.append(y['Start_Time'])
			start_hr = int(y['Start_Time'][10:13])
    			date_time_obj = datetime.strptime(y['Start_Time'], '%Y-%m-%d %H:%M:%S')
    			print(start_hr)
    			



