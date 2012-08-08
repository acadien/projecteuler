#!/usr/bin/python

from helper import primes2toN

bigN=int(12)
primes=primes2toN(bigN)

totalfacs=bigN-1
for i in range(2,bigN):
    if i in primes:
        totalfacs+=bigN-i-(bigN-i)/i
print totalfacs
