#!/usr/bin/python

from math import *
import operator
import numpy

def numpy_sieve(limit):
    is_prime = numpy.ones(limit + 1, dtype=numpy.bool)
    for n in xrange(2, int(limit**0.5 + 1.5)):
        if is_prime[n]:
            is_prime[n*n::n] = 0
    return numpy.nonzero(is_prime)[0][2:]

def primedecompose(a):
    global primes

    if a==0:
        return []

    subs=list()
    while True:
        if a==1:
            break
        for i in primes:
            if a%i==0:
                subs.append(i)
                a/=i
                break
    return list(set(subs))

def getphi(n):
    return int(n*reduce(operator.mul,[1-1/float(j) for j in primedecompose(n)]))

global primes,phi
primes=numpy_sieve(1E6)

phi=list()

sm=2#999500
lg=100#1000000
for i in range(sm,lg):
    phi.append(getphi(i))
print phi


print "Solution= 2*3*5*7*11*13*17=510510"

