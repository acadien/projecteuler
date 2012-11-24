#!/usr/bin/python
from math import *

def isincrease(n):
    n=[int(i) for i in str(n)]
    if len([1 for d0,d1 in zip(n[1:],n[:-1]) if d0-d1<0])>0:
        return False
    return True

def isdecrease(n):
    n=[int(i) for i in str(n)]
    if len([1 for d0,d1 in zip(n[1:],n[:-1]) if d1-d0<0])>0:
        return False
    return True

def isbouncy(n):
    return not(isincrease(n) or isdecrease(n))

c=1000
bouncecount=525
while True:
    sc=str(c)
    order=10**(len(sc)-3)
    
    if isbouncy(int(sc[:3])):
        incr=order
    else:
        incr=sum([1 for i in range(c,c+order) if isbouncy(i)])

    #break condition
    rat=float(bouncecount+incr)/(c+order)
    if rat>=0.99:
        #Step up to the proper ratio
        while rat!=0.99:
            if isbouncy(c):
                bouncecount+=1
            rat=float(bouncecount)/(c)
            c+=1
        c-=1
        break

    #increment loop
    c+=order
    bouncecount+=incr

print c
