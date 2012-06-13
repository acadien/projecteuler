#!/usr/bin/python
from math import *

perims=dict()
for i in range(1E3):
    perims[i]=0
for a in range(1,5000):
    for b in range(a,5000):
        c=sqrt(a*a+b*b)
        if int(c)==c and a+b+c<1000:
            perims[a+b+c]+=1


e=perims.keys()
e.sort(cmp=lambda a,b: cmp(perims[a],perims[b]))
print e[-1]
