#!/usr/bin/python
from math import *

def tri(n):
    return n*(n+1)/2

def pent(n):
    return n*(3*n-1)/2

def istri(a):
    n=int(sqrt(a*2))
    if n*(n+1)==a*2:
        return True
    return False

def hexa(n):
    return n*(2*n-1)

for i in range(144,100000):
    c=hexa(i)
    if istri(c):
        print i
        for j in range(i,100000):
            b=pent(j)
            if b>c: break
            if b==c:
                print c
                exit(0)
