#!/usr/bin/python
from math import *

def chain(n):
    #n=str(n)
    while True:
        #n=sum([int(i)**2 for i in n])
        #print [i**2 for i in map(int,str(n))]
        n=sum([i**2 for i in map(int,str(n))])
        if n==1: return False
        if n in [145,42,20,4,16,37,58,89]: return True
        #n=str(n)

t=0
for i in range(2,1E7):
    if chain(i):
        t+=1
    if i%1E6==0:
        print t
print t

