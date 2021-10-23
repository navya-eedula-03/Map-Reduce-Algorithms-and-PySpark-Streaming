#!/usr/bin/env python3
import os
import sys

Dict={}
path = sys.argv[1]

f1=open(path,'w+')


a=set()
for line in sys.stdin:
    line=line.strip()
    key,val=line.split(' ')
    key,val=int(key),int(val)
    a.add(key)
    a.add(val)
    if key in Dict:
        Dict[key].append(val)
    else:
        Dict[key]=[val]

for i in a:
    if( i in Dict):
        print(i,Dict[i])
    f1.write(str(i)+",1\n")

f1.close()
