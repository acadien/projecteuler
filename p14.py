#!/usr/bin/python
from math import *

def seq(n):
    if n%2==0:
        return n/2
    return 3*n+1

n=13
longest=506
i=800000
while(i<900000):
    i+=1
    l=0
    n=i
    while(True):
        n=seq(n)
        l+=1
        if n==1:
            break
    if(l>longest):
        longest=l
        print i,l
