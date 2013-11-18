#!/usr/bin/python

from math import *
from numpy import zeros
import pylab as pl
solved=False
N=1000
maxtiles=1000000
count = 0
width=0
ntiles=zeros([maxtiles])
for gapR in range(1,maxtiles/2):
    if solved: break

    for width in range(1,N):
        tiles=4*width*(gapR+width)
        if tiles <= maxtiles:
            ntiles[tiles-1]+=1
            count+=1
        else:
            if width==1:
                solved=True
            break

nn=ntiles.tolist()
print sum([nn.count(i) for i in range(1,11)])
