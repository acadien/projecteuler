#!/usr/bin/python
from math import *

def check_prime(x,primes):
    for i in primes:
        if x%i==0:
            return False
    return True

def f(n,a,b):
    return n*(a+n)+b

primes=list()
i=1
while len(primes)<1001:
    i+=1
    if check_prime(i,primes):
        primes.append(i)

maxcnt=0
maxa=0
maxb=0

print "Starting:"
for a in range(-1000,1000):
    for b in range(-1000,1000):
        n=0
        while f(n,a,b) in primes:
            n+=1
        if n>maxcnt:
            maxcnt=n
            maxa=a
            maxb=b
            print n,a,b

print maxcnt,maxa*maxb
