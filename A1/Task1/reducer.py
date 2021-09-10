#!/usr/bin/env python
"""reducer.py"""

import sys

l=[]
# input comes from STDIN
#print(type(sys.stdin))
for line in sys.stdin:
    	
    # remove leading and trailing whitespace
    line = line.strip()
    #print(line)
    l.append(int(line))
l.sort()

s=set(l)
la=[]
la=sorted(list(s))
#print(la)
for i in la:
	print(i,l.count(i))
