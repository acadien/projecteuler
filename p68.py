#!/usr/bin/python
from math import *
from random import *
from itertools import chain,permutations

o_ind=range(5)
i_ind=[[5,6],[6,7],[7,8],[8,9],[9,5]]

def trysum(A):
    if 10 in A[5:]:
        return False
    B=set([A[i]+A[i_ind[i][0]]+A[i_ind[i][1]] for i in range(5)])
    if len(B)==1:
        return True
    return False

def flatten(listOfLists):
    return chain.from_iterable(listOfLists)

def tochain(A):
    start=A.index(min(A[:5]))
    return int("".join(map(str,flatten([[A[o_ind[j]],A[i_ind[j][0]],A[i_ind[j][1]]] for j in map(lambda x:x%5,range(start,start+5))]))))
        
mx=0
for A in permutations(range(1,11)):
    if trysum(A):
        Aval=tochain(A)
        if Aval>mx:
            print Aval
            mx=Aval
    

