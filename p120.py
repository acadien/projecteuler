#!/usr/bin/python
from math import *

def crazyF(a,n):
    if n%2==0: return 2
    numer=(a-1)**n+(a+1)**n
    denom=a*a
    return numer%denom

global s
s=2
def test_repeat(seq):
    global s
    start=s
    l=len(seq)
    s=l/2
    for x in range(start,s):
        repeat=True
        for i in range(1,l/x):
            if seq[0:x] != seq[i*x:(i+1)*x]:
                repeat=False
                break
        if repeat: 
            return x
    return -1
        

maxr=[]
step=100
for a in range(3,1001):
    print a
    remains=list() 
    cnt=0
    while True:
        remains+=map(lambda x:crazyF(a,x),range(cnt,cnt+step))        
        if test_repeat(remains)>0:
            maxr.append(max(remains))
            break
        if step>1E6:
            print a,"stuck here"
            exit(0)
        cnt+=step
    print cnt
print sum(maxr)

        

