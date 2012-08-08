#!/usr/bin/python
from math import *

def check_paldrm(x):
    pal=str(x)
    for i in range(len(pal)/2+1):
        if pal[i]!=pal[-(i+1)]:
            return False
    return True

tot=0
for i in range(1E6+1):
    if check_paldrm(i) and check_paldrm(bin(i)[2:]):
        tot+=i
print tot

