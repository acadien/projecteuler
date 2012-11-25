#!/usr/bin/python
from math import *

#Returns 0 if not amicable, otherwise returns the pair
def amicable(n):
    divs=list()
    divs = sum([i for i in range(1,n/2+1) if n%i==0])
    if sum([i for i in range(1,divs/2+1) if divs%i==0])==n:
        return divs
    return 0

amics=list()
for i in range(1,10001):
    if i in amics: continue
    nami=amicable(i)
    if i==nami:
        continue
    elif nami!=0:
        amics.append(i)
        amics.append(nami)
print amics
print sum(amics)
