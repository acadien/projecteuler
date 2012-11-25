#!/usr/bin/python
from math import *

a=3.0/7.0

m=-1000
win=0
for i in range(1,1e6):
  b=round(float(i)*a,0)/i-a 
  if b<0 and b>m:
      m=b
      win=round(float(i)*a,0)

print win
