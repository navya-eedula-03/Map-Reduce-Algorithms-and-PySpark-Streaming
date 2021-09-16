#!/usr/bin/env python3
"""reducer.py"""

import sys

l=[]
state=""
city=""
cc=1
sc=1
lc=0
for line in sys.stdin:
	if lc==0:
		#print("i st line")
		line = line.strip()
		l=line.split(" ",1)
		state=l[0]
		print(state)
		city=l[1]
		sc=1
		cc=1
		lc+=1
	else:
		line=line.strip().split(" ",1)
		#print(state,type(state))
		if str(line[0])==state:
			#print("in")
			sc+=1
			if line[1]==city:
				cc+=1
			else:
				print(city,cc)
				cc=1
				city=line[1]
				#print("chan city")
		else:
			print(city,cc)
			
			print(state,sc)
			sc=1
			state=line[0]
			#print("change state")
			cc=1
			print(state)
			city=line[1]
print(city,cc)
print(state,sc)    		
