#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
import json


l=[]
d={}
# input comes from STDIN
#print(type(sys.stdin))
for line in sys.stdin:
    	
    # remove leading and trailing whitespace
    line = line.strip()
    #print(line)
    l=line.split(":")
    if(l[0] in d):
    	d[l[0]].append(l[1])
    else:
    	d[l[0]]=[l[1]]
    #print(d)
#print(d)
for i,j in d.items():
	s=set(j)
	sl=sorted(list(s))
	print(i)
	sa=0
	for k in sl:
		print(k,j.count(k))
		sa+=j.count(k)
	print(i,sa)