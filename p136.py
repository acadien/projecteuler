#!/usr/bin/python
from math import *

def a(n):
    d=sqrt(n/4)
    if int(d)==d:
        print "hi"
        return True
    d=int(d)+1
    sq=sqrt(4*d*d-n)
    fnd=False
    while True:
        while int(sq)!=sq:
            d+=1
            sq=sqrt(4*d*d-n)
            a1=2*d-sq
            a2=2*d+sq
            print d,a1,a2
            if 2*d-sq<1:
                break
            if 4*a2*d-a2*a2>n:
                return False
        a1=2*d-sq
        a2=2*d+sq
        if a1<d:
            return True
        return False

print sum([1 for i in range(100) if a(i)])
    
