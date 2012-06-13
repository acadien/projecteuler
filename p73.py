#!/usr/bin/python
from math import *
from fractions import Fraction

#a little googling reveals the Farey Sequence.
#next term given the previous two terms are a/b and c/d:
#p=k*c-a
#q=k*d-b
#where k=floor((n+b)/d)

dlimit=12000

a=1
b=3
c=4000 #the next closest ratio
d=11999

total=0
while float(c)/d<0.5:
    k=int(float(dlimit+b)/d)
    a,b,c,d=c,d,k*c-a,k*d-b
    total+=1
print total
