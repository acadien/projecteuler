#!/usr/bin/python

import numpy

def numpy_sieve(limit):
    is_prime = numpy.ones(limit + 1, dtype=numpy.bool)
    for n in xrange(2, int(limit**0.5 + 1.5)):
        if is_prime[n]:
            is_prime[n*n::n] = 0
    return numpy.nonzero(is_prime)[0][2:]

def check_cons(primes,limit,strt):
    mxcnt=-1
    mxmin=0
    mxind=0
    cnt=0
    val=0
    min=0
    for (ind,i) in enumerate(primes):
        if i>limit/2 or min>10:
            return (mxmin,mxind,mxcnt)
        if val==0:
            min=ind
        val+=i
        cnt+=1
        while val>limit:
            val-=primes[min]
            min+=1
            cnt-=1
        if val==limit:
            if cnt > mxcnt:
                mxcnt=cnt
                mxmin=min
                mxind=ind

primes=numpy_sieve(1E6)
rprimes=primes.tolist()
rprimes.reverse()
mxcnt=-1
strt=0
for i in rprimes:
    (mi,mx,c)=check_cons(primes,i,strt)
    strt=mx
    if c>mxcnt:
        print mi,mx,c,i
        mxcnt=c
