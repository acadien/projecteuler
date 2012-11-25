#!/usr/bin/python
from math import *
import re

low =int(sqrt(1020304050607080900))
high=int(sqrt(1929394959697989909))

def compare(val):
    val=str(val)
    if val[::2]=="1234567890":
        return True
    return False

print 

prev=low
step=1000000
while True:
    for i in range(prev,prev+step):
        if i%1000==0:
            print high-i
        if compare(i*i):
            print i
            exit(0)
    prev+=step
