#!/usr/bin/env python3
Dict={}
import sys
f1=open('/home/pes1ug19cs433/Desktop/BIG_DATA/Big-Data-Sem-5/A2/Task1/v.txt','w+')

for line in sys.stdin:
    line=line.strip()
    key,val=line.split(' ')
    key,val=int(key),int(val)
    if key in Dict:
        Dict[key].append(val)
    else:
        Dict[key]=[val]

for i in Dict:
    print(i,Dict[i])
    f1.write(str(i)+",1\n")

f1.close()
