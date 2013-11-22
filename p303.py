#!/usr/bin/python

from numpy import zeros

maxN=10000
fn=zeros(maxN)
for n in range(1,maxN+1):
  mul=1
  while max(str(n*mul))>'2':
    mul+=1
  print n,mul
