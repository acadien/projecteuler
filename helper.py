#!/usr/bin/python

#Calculate some primes
def primes2toN(max_n):
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

#Factoriez numbers less than 1E7
#primes=primes2toN(int(1E7))
def factorize(N,primes):
 #   if N>1E7:
 #       print "Need to increase maximum primes list to properly factorize"
    if N<2:
        return []
    if N in primes:
        return [N]
    facs=list()
    a=primes[0]
    q=0
    while N!=1:
        while N%a==0:
            facs.append(a)
            N/=a
        q+=1
        a=primes[q]
    return facs
