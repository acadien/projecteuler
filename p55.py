#!/usr/bin/python
from math import *

def check_paldrm(x):
    pal=str(x)
    for i in range(len(pal)/2+1):
        if pal[i]!=pal[-(i+1)]:
            return False
    return True

def lych(n):
    l=int(str(n)[::-1])
    return n+l

MAXITER=50
tot=0
for i in range(int(1E4)):
    n=i
    fnd=0
    for j in range(MAXITER):
        n=lych(n)
        if check_paldrm(n):
            print n,j
            fnd=1
            break
        
    if fnd==0:
        tot+=1

print tot
