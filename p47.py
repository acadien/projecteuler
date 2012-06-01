#!/usr/bin/python

import numpy

def numpy_sieve(limit):
    is_prime = numpy.ones(limit + 1, dtype=numpy.bool)
    for n in xrange(2, int(limit**0.5 + 1.5)):
        if is_prime[n]:
            is_prime[n*n::n] = 0
    return numpy.nonzero(is_prime)[0][2:]

def primefactorlen(primes,val,n):
    i=0
    facts=set([])
    while True:
        prm=primes[i]
        if prm>val:
            return False
        while val%prm==0:
            val/=prm
            facts |= set([prm])
        if val==1 and len(facts)==n:
            return True
        i+=1
        
primes=numpy_sieve(1E6).tolist()

nconsecs=4
consecs=list([0])*nconsecs
conind=0

i=10000
while True:
    i=i+1
    if primefactorlen(primes,i,nconsecs):
        consecs[conind]=i
        conind+=1
        print i,conind
        if conind==nconsecs:
            print consecs
            exit(0)
    else:
        conind=0
