#!/usr/bin/python
from math import *
from numpy import *

#reduce the fraction
def reduceFrac(numer,denom):
    for i in range(2,min([numer,denom])+1):
        while numer%i == 0 and denom%i==0:
            numer/=i
            denom/=i
        if i>numer or i>denom:
            break
    return numer,denom


bignum=50
cnt=bignum*bignum*3 #right triangles with p1 and p2 at sides of square, rotation gives you *3

#loop over a point inside the square
for i in range(1,bignum+1):
    for j in range(1,bignum+1):
        #Using the slope of this line, count how many have the inverse negative slope (cut off at edge of square)
        a,b=reduceFrac(i,j)

        #multiply by two for symmetry
        tri1=j/a*2                #cut off at y
        tri2=(bignum-i)*i/a/j*2   #cut off at x
        if tri1<tri2:
            cnt+=tri1
        else:
            cnt+=tri2
print cnt
