#!/usr/bin/python
from math import *
import sys

#Returns a string made of the numbers from num to num+JUMP
def fetch(num,JUMP):
    strn=""
    for i in range(num,num+JUMP):
        strn+=str(i)
    return strn

ll=fetch(0,1E6)
print int(ll[1])*int(ll[10])*int(ll[100])*int(ll[1000])*int(ll[10000])*int(ll[100000])*int(ll[1000000])
