#!/usr/bin/python
from math import *

def pentagfrom1to(n):
    mx=(1+sqrt(1+4*3*2*n))/6
    return [i*(3*i-1)/2 for i in range(mx+1)]
        
pentags=pentagfrom1to(1E7)
N=len(pentags)

for i,a in enumerate(pentags):
    for b in pentags[i+1:]:
        if a+b in pentags[i+1:]:
            print a,b,a+b
            if b-a in pentags:
                print a,b,a+b,b-a
                break
