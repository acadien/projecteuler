#!/usr/bin/python
from math import *
from numpy import *

mxnum=2e6

#makin rectangles... awww yeah
sz=2100

rectrect=zeros((sz,sz))

rectrect[1,1]=1
for i in range(2,sz):
    rectrect[1,i]=rectrect[1,i-1]+i

for j in range(2,sz):#sz
    wid=rectrect[1,j]
    for i in range(j,sz):#sz
        if wid*rectrect[1,i] > mxnum+1000:
            break
        rectrect[j,i]=wid*rectrect[1,i]
        if abs(rectrect[j,i]-mxnum)<100:
            print i*j,rectrect[j,i]


