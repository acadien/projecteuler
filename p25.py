#!/usr/bin/python
from math import *

def fib(n1,n2):
    return n1+n2

f1=1
f2=1

k=2
while(True):
    k+=1
    f3=fib(f1,f2)
    f1=f2
    f2=f3
    if len(str(f2))>=1000:
        break
    

print k
