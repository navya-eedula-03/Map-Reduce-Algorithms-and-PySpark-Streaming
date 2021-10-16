#!/usr/bin/env python3
import sys
import os

for line in sys.stdin:
    line=line.strip()
    key,val=line.split('\t')
    print(int(key),int(val))
