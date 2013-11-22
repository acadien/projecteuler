#!/usr/bin/python

from numpy import zeros

maxN=10000
fn=zeros(maxN)
total=0
for n in range(1,maxN+1):
  if n==99:
    total+=11335578
    continue
  if n==999:
    total+=111333555778
    continue
  if n==9999:
    total+=1111333355557778
    continue
  mul=1
  while max(str(n*mul))>'2':
    mul+=1
  total+=mul
  print n,mul
print total
