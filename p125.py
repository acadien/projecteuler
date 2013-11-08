#!/usr/bin/python
from math import *
#mine
from PEutil import *

bignum=10**8
smallnum=int(sqrt(bignum))+1

#loop over starting points
e=0
pals=list()
for i in range(1,smallnum+1):
    tot=i*i
    for j in range(i+1,smallnum+1):
        tot+=j*j
        if tot>bignum: break
        if palindrome(tot):
            if tot in pals:
                continue
            pals.append(tot)
            e+=tot
print e
