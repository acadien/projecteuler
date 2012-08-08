#!/usr/bin/python
from math import *


maxx=0
for a in range(100):
    for b in range(100):
        x=sum([int(i) for i in str(a**b)])
        if x>maxx:
            print a,b,x
            maxx=x
print maxx
