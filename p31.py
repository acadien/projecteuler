#!/usr/bin/python
from math import *

coins=[1,2,5,10,20,50,100,200]

val=200
def getcnt(n,i):
    if n==0: return 1
    if n<0: return 0
    return sum([getcnt(n-coin,j+1) for (j,coin) in enumerate(coins[:i])])

print getcnt(val,len(coins))
   

