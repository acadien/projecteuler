#!/usr/bin/python
from math import *
import primes
from itertools import product
N=10**6
NN=len(str(N))-1
prms=[str(i) for i in primes.primesfrom2to(N) if i>N/10]
masks= [''.join([str(x) for x in i]) for i in product(range(2),repeat=NN)][1:-1]

ignore=set()

for prm in prms:
    for mask in masks:
        pat=''.join(['x' if i=='1' else c for c,i in zip(prm,mask)])
        if pat not in ignore: ignore.add(pat)
        else: continue
        count=0
        for i in range(10):
            if ''.join([str(i) if m =='1' else p for p,m in zip(prm,mask)]) in prms: count+=1
        if count>4:
            print count,pat
        if count==8:
            print pat
            exit(0)
