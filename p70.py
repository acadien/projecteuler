#!/usr/bin/python

from math import *
from primes import *

#phi(87109) = 79180

N=10**7

def ispermute(a,b):
    a=str(a)
    b=list(str(b))
    if len(a)!=len(b):
        return False
    for i in a:
        try:
            b.remove(i)
        except ValueError:
            return False
    return True

primes=primesfrom2to(10**4)

mn=100000
for i,vi in enumerate(primes):
    for vj in primes[i:]:
        phi=(vi-1)*(vj-1)
        n=vi*vj
        a=float(n)/phi
        if a<mn and n<10**7 and ispermute(n,phi):
            mn=a
            mnn=n
            mnphi=phi
            print a,n,phi
