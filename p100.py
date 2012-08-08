#!/usr/bin/python

from decimal import *
from math import sqrt
getcontext().prec = 100

g=Decimal('1.8E12')
g=Decimal('10')
g=0
def bary(y):
#    y=Decimal(y)
    return (g+y)*(g+y-1)

def barx(x):
    x=Decimal(x)
    return 2*x*(x-1)

def foo(x,y):
    return barx(x)-bary(y)

t=Decimal('-0.5')
t=-0.5
def quad(a,b,c):
    s=sqrt(4.-8.*c)/4.
    return s-t

a=2
b=-2

one=Decimal('1')
for y in range(int(1E7)):
    c=-bary(y)
    x=quad(a,b,c)
    if x%1==0:
        print x,g+y,foo(x,y)
    
    

