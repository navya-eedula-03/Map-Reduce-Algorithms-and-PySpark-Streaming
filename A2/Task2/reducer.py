#!/usr/bin/env python3
import sys

Dict2 ={}
for line in sys.stdin:

    line = line.strip()
    key1,key2,value =line.split(' ',2)
    key1,key2,value=int(key1),str(key2),float(value)
    if key2 in Dict2:
        Dict2[key2]+=0.85*value
    else:
        Dict2[key2]=0.85*value

for key in sorted(Dict2.keys()):
    Dict2[key]+=0.15
    print("%s,%1.2f "%(key,Dict2[key]))
