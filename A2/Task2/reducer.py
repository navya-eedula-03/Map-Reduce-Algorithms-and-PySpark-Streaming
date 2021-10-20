#!/usr/bin/env python3
import sys

Dict2 ={}
for line in sys.stdin:

    line = line.strip()
    key1,key2,value =line.split(' ',2)
    key1,key2,value=int(key1),int(key2),float(value)
    if key2 in Dict2:
        Dict2[key2]+=0.85*value
    else:
        Dict2[key2]=0.85*value

f1=open('V1.txt','w+')
for key in Dict2:
    Dict2[key]+=0.15
    print("%d,%1.2f "%(key,Dict2[key]))
    f1.write("%d,%1.2f\n"%(key,Dict2[key]))
