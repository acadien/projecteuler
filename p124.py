#!/usr/bin/python

from math import *
import operator
#mine
from PEutil import *

#function returns the radical (the product of the distinct prime factors) of n
def radical(n,primes):
    if n<=3: return n
    if n%100==0:
        print n
    facs=list()
    for i in primes:
        if n%i==0:
            facs.append(i)
            n/=i
        while n%i==0:
            n/=i
        if n==1:
            return product(facs)
        if i>n: break
    return 100000

#Brute force. why? because it works.
bignum=100000
smallnum=10000

primes=primesfrom2to(smallnum)
rads=map(lambda x:radical(x,primes),range(1,bignum))
srads=sorted(zip(range(1,bignum),rads),key=lambda x:x[1])
print srads[smallnum-2]
