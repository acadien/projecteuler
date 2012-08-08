#!/usr/bin/python
from math import sqrt
from decimal import *

getcontext().prec = 102

def getdecsum(i):
    a=str(Decimal(i).sqrt())
    if float(a)==int(sqrt(i)):
        return 0
    return sum([int(j) for j in str(a)[:101] if j.isdigit()])

print sum([getdecsum(i) for i in range(101)])

