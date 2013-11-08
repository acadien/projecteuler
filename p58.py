#!/usr/bin/python
from math import *
#mine
from PEutil import *

layer=0
num=1
total=1
count=0
while True:
    total+=4
    layer+=2
    num+=layer
    for i in range(1,4):
        if isprime(num):
            count+=1
        num+=layer
    if float(count)/total < 0.1:
        print '='*25
        print layer+1
        print '='*25
        break




