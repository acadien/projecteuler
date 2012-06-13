#!/usr/bin/python
from math import *
from fractions import gcd

#Runs in 7 seconds

#Problem 75
mx=866
maxval=1500000
cnt=0
pytriples=dict()
uniq=set()
for m in range(1,mx):
    for n in range(1,m):
        a0=m*m-n*n
        b0=2*m*n
        c0=m*m+n*n
        if gcd(a0,b0)!=1:
            continue #Check for coprimity of m and n
        if (m-n)%2==0:
            continue #
        #if a0+b0+c0>maxval:
        #    break
        #if b0<=a0: #Swap a and b so a<b
        #    temp=b0
        #    b0=a0
        #    a0=temp
        for k in range(1,int(maxval/c0)):
            a=a0*k
            b=b0*k
            c=c0*k
            if a+b+c>maxval:
                break
            s="%d|%d|%d"%(a,b,c)
            if s in uniq:
                continue
            else:
                uniq.add(s)
            L=a+b+c
            pytriples[L]=pytriples.setdefault(L,0)+1

#Get only the pytriples that are found once
print sum([1 for key in pytriples.keys() if pytriples[key]==1])
