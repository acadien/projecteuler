#!/usr/bin/python
from math import *
import numpy
#mine
from PEutil import *

primes=primesfrom2to(1E5)

val=int(1E5)



lasti=0
maxindex=0
maxprime=2
for v in range(2,val):
  counters=[0 for i in range(v+1)]
  counters[0]=1
  if v>primes[-1]:
    print "need more primes"
    exit(0)

  for p in primes:
    if p>v: break
    for j in range(p,v+1):
      counters[j]+=counters[j-p]

  if v%100==0:
    print v

  if counters[v]>5000:
    print counters[:v+1]
    print "win",v
    break
