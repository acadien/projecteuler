#!/usr/bin/python
from math import *

nums=list()
for i in range(10):
    nums.append(str(i))
print nums
final=list()

maxv=1000000
for j in range(9,-1,-1):
    #if maxv==0:
    #    print nums.pop()
    #    continue
    for i in range(10):
        if maxv-i*factorial(j)<=0:
            break
        
    maxv-=(i-1)*factorial(j)
    print nums.pop(i-1)
