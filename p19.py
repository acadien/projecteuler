#!/usr/bin/python
from math import *

sumtot=0
for i in range(2,1000000):
    ii=str(i)
    tot=0
    for let in ii:
        tot+=int(let)**5
    if tot==i:
        sumtot+=tot
        print tot

print sumtot
