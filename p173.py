#!/usr/bin/python

from math import *

solved=False
N=1000
maxtiles=1000000
count = 0
width=0
for gapR in range(1,maxtiles/2):
    print gapR,width
    if solved: break

    for width in range(1,N):
        if 4*width*(gapR+width) <= maxtiles:
            count+=1
        else:
            if width==1:
                solved=True
            break

print count
