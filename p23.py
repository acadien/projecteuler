#!/usr/bin/python
from math import *

def abundant(x):
    return sum([i+x/i for i in range(2,int(sqrt(x))+1) if x%i==0])+1>x

abunds=[i for i in range(1,28124) if abundant(i)]
oddabunds=[i for i in abunds if i%2==1]

def sumabund(x):
    if x%2==1:#odd
        for a in abunds:
            if x<=a: return False
            for b in oddabunds:
                if x==a+b: return True
    else:
        for a in abunds:
            if x<=a: return False
            for b in abunds:
                if x==a+b: return True
    return False


tot=0
for i in range(1,28124):
    if not(sumabund(i)):
        tot+=i
        print i,tot


