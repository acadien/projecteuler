#!/usr/bin/python
from math import *


def tribo(b,a=0):
    Ts=[1,1,1]
    t=list()
    for i in range(a,b):
        Ts.append(sum(Ts))
        t.append(Ts[-1])
        Ts.pop(0)
    return t

cnt=1
k=27
tribs1=tribo(11100)
tribs2=tribo(12100)
while True:
    fnd=False
    for i in tribs2:
        if k%i==0:
            fnd=True
            break
    k+=2
    if not fnd:
        cnt+=1
        print cnt,k
    if cnt==124:
        break
