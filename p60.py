#!/usr/bin/python
from math import *
from itertools import permutations
#mine
from PEutil import *
n=1E4
primes=primesfrom2to(n).tolist()
primes.remove(2)
primes.remove(5)

px=dict()
for i in range(len(primes)):
    p=primes[i]
    px[p]=set()
    for j in range(i,len(primes)):
        q=primes[j]
        if isprime(int(str(q)+str(p))) and isprime(int(str(p)+str(q))):
            px[p].add(q)
               
for xx in px:
    for ax in px[xx]:
        seta=px[xx] & px[ax]
        if len(seta)>0:
            for bx in seta:
                setb=seta & px[bx]
                if len(setb)>0:
                    for cx in setb:
                        setc=setb & px[cx]
                        if len(setc)>0:
                            print xx,ax,bx,cx,setc
"""for a in px:
                for e in rprimes:
                    vals=[int(''.join([str(j) for j in i])) for i in permutations([a,b,c,d,e],2)]
                    print vals
                    exit(0)
#                if len([i for i in vals if not(i in bigprimes)])==0:
#                    print a,b,c,d
                    if len([i for i in vals if not(isprime(i))])==0:
                        print a,b,c,d,e
                        exit(0)




"""
