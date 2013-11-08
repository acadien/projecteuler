#!/usr/bin/python
from math import *
from PEutil import *

def cg(n,prms):
    for i in prms:
        if i>=n:
            break
        for j in range(1,sqrt(n/2)+1):
            j*=j
            if i+2*j==n:
                return True
    return False


prms=primesfrom2to(100000)

i=9
while True:
    i+=2
    l=[j for j in range(2,i) if i%j==0]
    if any(l):
        print i
        if not cg(i,prms):
            print i
            break

