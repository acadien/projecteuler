#!/usr/bin/python
from math import sqrt

def tottri(n):
    return sum(range(n+1))

def nfac(n):
    num=n
    i=1
    nfacs=0
    while i<sqrt(num):
        if num%i==0:
            nfacs+=1
        i+=1
    
    return nfacs*2

k=10000
j=tottri(j)
while(k<20000):
    k+=1    
    j+=k
    c=nfac(j)
    print j,c
    if c>=500:
        break

print j
