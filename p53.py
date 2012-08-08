#!/usr/bin/python
from math import *
from operator import mul

choose= lambda n,r: reduce(mul,range(r+1,n+1))/reduce(mul,range(1,n-r+1))

tot=0
for n in range(1,101):
    for r in range(1,n):
        if choose(n,r)>1E6:
            tot+=1

print tot
    
