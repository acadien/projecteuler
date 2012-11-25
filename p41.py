#!/usr/bin/python
from math import *

import numpy

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def pandig(n):
    n=str(n)

    for dig in n:
        if dig==9 or dig==8 or dig==0:
            return False
    digs=range(1,len(n)+1)
    for dig in n:
        d=int(dig)
        if d in digs:
            digs.pop(digs.index(d))
        else:
            print n,digs
            return False
    return True

prms=primesfrom2to(8E6).tolist()
prms.reverse()

for i in prms:
    if pandig(i):
        print i
        break
