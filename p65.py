#!/usr/bin/python
from math import *

#reduces a fraction by 1
def reduce_frac(denoms,lnumer,ldenom):
    return denoms[:-1],ldenom,lnumer+ldenom*denoms[-1]

def convergents(denoms):
    ldenom=denoms.pop()
    lnumer=1
    while(len(denoms)>0):
        denoms,lnumer,ldenom=reduce_frac(denoms,lnumer,ldenom)
    return ldenom,lnumer #swapped

#build the e-list
e_vals=[2,1,2]
for k in range(2,100):
    e_vals+=[1,1,2*k]

print sum(map(int,str(convergents(e_vals[:100])[0])))
