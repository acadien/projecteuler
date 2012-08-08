#!/usr/bin/python
from math import *

base=list()
exp=list()
for line in open("base_exp.txt","r").readlines():
    line=[float(i) for i in line.split(",")]
    base.append(line[0])
    exp.append(line[1])

x=10000.0
y=500000.0
big=list()
for b,e in zip(base,exp):
    b2=b/(x**(y/e))
    e2=e/10000.0
    big.append(b2**e2)

print big.index(max(big))+1
