#!/usr/bin/python
from math import *


def pandig(n):
    for dig in n:
        if dig==9 or dig==8 or dig==0:
            return False
    digs=range(1,len(n)+1)
    for dig in n:
        d=int(dig)
        if d in digs:
            digs.pop(digs.index(d))
        else:
            return False
    return True

tot=0

pandis=list()
for i in range(1,1E5):
    n=''
    for dig in str(i):
        if dig not in n:
            n+=dig
    pandis.append(i)

for (place,i) in enumerate(pandis):
    for j in pandis[place+1:]:
        comb=str(i)+str(j)+str(i*j)
        if len(comb)!=9:
            continue
        if pandig(comb): 
            tot+=i*j
            print i*j,comb
print tot

