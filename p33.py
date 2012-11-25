#!/usr/bin/python
from math import *

totded=1
totnum=1
for i in range(10,100):
    for j in range(i,100):
        a=str(i)
        b=str(j)
        a0=float(a[0])
        a1=float(a[1])
        b0=float(b[0])
        b1=float(b[1])
        i=float(i)
        j=float(j)
        if b1==0: continue
        
        if i/j==a0/b1 and i/j==a1/b0: continue
        if i/j==a0/b1 and a1==b0:
            totnum*=i
            totded*=j
            print a,b,i/j,a0/b1
        if i/j==a1/b0 and a0==b1:
            totnum*=i
            totded*=j
            print a,b,i/j,a1/b0


print totnum/totded
