#!/usr/bin/env python3

def modp(li):
    sum=0
    for i in li:
        sum+=i*i
    return sum**0.5
import sys 
import json
l=[]
f1=open('output.txt','r')
f2=open('embedding-sample.json','r')
y=json.loads(f2.read())

for line in f1.readlines():
    line=line.strip()
    key,val=line.split(' ',1)
    val=val[1:-1]
    if ',' in val:    vall=list(map(int,val.split(',')))
    else: vall=[int(val)]
    l=len(vall)
    for i in vall:
        #print(key,i,1/l)
        dp=sum([ (y[str(key)][k]*y[str(i)][k]) for k in range(0,5)])
        temp=dp/(modp(y[str(key)])*(modp(y[str(i)])))
        #print(1/l,temp)
        print(key,i,temp*(1/l))
        #print(dp)        

