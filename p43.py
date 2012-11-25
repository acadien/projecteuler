#!/usr/bin/python
from math import *
from itertools import permutations,combinations

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

def check_div3(N):
    #check div 2
    #c2=int(N[3])%2==0
    c3=int(N[2:5])%3==0
    #c5=int(N[5])==5
    c7=int(N[4:7])%7==0
    c11=int(N[5:8])%11==0
    c13=int(N[6:9])%13==0
    c17=int(N[7:10])%17==0
    return c3 and c7 and c11 and c13 and c17

#print check_div3("1406357289")
pandis=list()
digs=[str(i) for i in range(10)]

for dig3 in ['0','2','4','6','8']:
    if dig3=='0':
        dig5='5'
        ldgs=[i for i in digs if i!=dig3 and i!=dig5]
        pandis+=[str(''.join(ln[0:3])+dig3+''.join(ln[3:4])+dig5+''.join(ln[4:])) for ln in permutations(ldgs)]
    else:
        for dig5 in ['0','5']:
            ldgs=[i for i in digs if i!=dig3 and i!=dig5]
            pandis+=[str(''.join(ln[0:3])+dig3+''.join(ln[3:4])+dig5+''.join(ln[4:])) for ln in permutations(ldgs)]


print sum([int(pd) for pd in set(pandis) if check_div3(pd)])

