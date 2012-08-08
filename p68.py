#!/usr/bin/python
from math import *

o_ind=range(5)
i_ind=[[5,6],[6,7],[7,8],[8,9],[9,5]]

def checkEqual6502(lst):
    return not lst or [lst[0]]*len(lst) == lst

def trysum(A):
    B=[A[i]+A[i_ind[i][0]]+A[i_ind[i][1]] for i in range(5)]
    return checkEqual6502(B)


    

A=range(1,11)
print trysum(A)  


