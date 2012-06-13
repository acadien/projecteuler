#!/usr/bin/python
import operator
#mine
from primes import primesfrom2to

#Using the Farey Sequence length (function of euler totient)
N=int(1E6)

def eulerTotient(n,factors):
    factors=list(set(factors))
    return n*reduce(mul,map(lambda x: 1.0-1.0/x,factors))

primes=map(int,primesfrom2to(N**0.5*10))
print type(primes[0])
#bigprimes=primesfrom2to(N)
def factor(n):
   x=0
   i = primes[x]
   limit = n**0.5
   while i <= limit:
     if n % i == 0:
       yield i
       n = n / i
       limit = n**0.5
     else:
       x += 1
       i=primes[x]
   if n > 1:
       yield n
f=0 #F1=2 but euler doesn't want 0/1 and 1/1
for n in range(2,1000001):
 s=n*reduce(operator.mul,[(1.-1./x) for x in list(set(factor(n)))])
 f+=s
print "%20d"%f
"""
euTots=1
for i in range(3,N+1):
    factors=list(set(factorize(i)))
    euTots+=i*reduce(mul,map(lambda x: 1.0-1.0/x,factors))
print int(euTots)

"""
