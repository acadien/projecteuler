#!/usr/bin/python

from math import *

#Euler's generating function
def euler_gen(P):
    n=len(P)
    a=0
    for k in range(n):
        a=n-k*(3*k-1)/2
        b=n-k*(3*k+1)/2
        if a<0:Pa=0 
        else:  Pa=P[a]
        if b<0:Pb=0
        else:  Pb=P[b]
        if k%2==1:
            a+=(Pa+Pb)
        else:
            a-=(Pa+Pb)

    P.append(a)
    #P.append(sum([(-1**k) * (P[n-k*(3*k-1)/2]+P[n-k*(3*k+1)/2]) for k in range(1,n+1)]))

newlist=[1,1]
for i in range(2,10):
    euler_gen(newlist)
    print i,newlist[-1]

"""String Parsing version: very slow
def numsums(n,prevlist):
    newlist=list()
    for sumval,smalllist in enumerate(prevlist):
        sumval+=2
        diff=str(n-sumval)
        sumval=str(sumval)
        newlist.append(".".join(sorted([sumval,diff])))
        for i in smalllist:
            i=i.split(".")+[diff]
            newlist.append(".".join(sorted(i)))
    prevlist.append(list(set(newlist)))

dynlist=[["1.1"]]
for i in range(3,100):
    numsums(i,dynlist)
    print i,len(dynlist[-1])
print len(dynlist[98])
"""
