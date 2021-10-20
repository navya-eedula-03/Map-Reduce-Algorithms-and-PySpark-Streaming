#!/usr/bin/env python3
import sys

def modp(li):
    sum=0
    for i in li:
        sum+=i*i
    return sum**0.5
import sys 
import json
l=[]
emb_fi = sys.argv[1]
v_fi = sys.argv[2]
f2=open(emb_fi,'r')
f1=open(v_fi,'r')

y=json.loads(f2.read())

for line in sys.stdin:
    line=line.strip()
    key,val=line.split(' ',1)
    val=val[1:-1]
    if ',' in val:    vall=list(map(int,val.split(',')))
    else: vall=[int(val)]
    l=len(vall)
    for i in vall:
        dp=sum([ (y[str(key)][k]*y[str(i)][k]) for k in range(0,5)])
        temp=dp/(modp(y[str(key)])*(modp(y[str(i)])))
        print(key,i,temp*(1/l))
