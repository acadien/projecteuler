#!/usr/bin/python

def check_prime(x,primes):
    for i in primes:
        if x%i==0:
            return False
    return True

primes=list()
i=1
while len(primes)<10001:
    i+=1
    if check_prime(i,primes):
        primes.append(i)
        print i
    
print primes[-1]
