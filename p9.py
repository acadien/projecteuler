#!/usr/bin/python

from math import sqrt

def check_prime(x,primes):
    sqt=int(sqrt(x))
    for i in primes:
        if x%i==0:
            return False
        if i>sqt:
            primes.append(i)
            break
    return True

primes=list()
primes.append(2)
for i in range(3,2000000,2):
    if check_prime(i,primes):
        print i
print sum(primes)
