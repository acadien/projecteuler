#!/usr/bin/python
from math import *

cnt=0
for expo in range(1,200):
    for base in range(1,200):
        if len(str(base**expo))==expo:
            print base,expo
            cnt+=1

print cnt
