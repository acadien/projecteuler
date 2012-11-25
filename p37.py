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

prms=primesfrom2to(2E6)

print prms

def truncable(n):
    n=str(n)
    if int(n[0]) not in prms[0:4]: 
        return False
    for i in range(len(n)-1):
        #print n[i+1:],":",n[:i+1]
        if int(n[i+1:]) not in prms:
            return False
        if int(n[:i+1]) not in prms:
            return False
    return True

trncs=list()
for i in prms[4:]:
    if truncable(i):
        trncs.append(i)
        print i
        if len(trncs)==11:
            break

print sum(trncs)




