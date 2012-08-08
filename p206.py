#!/usr/bin/python
from math import *
import re

low=int(sqrt(1020304050607080900))
#high=int(sqrt(192939495969798999))

low +=   200000000
high=low+100000000

tomatch="1.2.3.4.5.6.7.8.9.0"
prog = re.compile(tomatch)

print low**2,len(str(low**2)),len("1.2.3.4.5.6.7.8.9.0")

for i in range(low,high):
    a=str(i**2)
    if a[2]=="2":# and a[4]=="3":
        if prog.match(a):
            print i,i**2
            break

print a
