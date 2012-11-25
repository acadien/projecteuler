#!/usr/bin/python
from math import *
from numpy import *

n=1001

tot=1
val=1
for i in range(3,n+1,2):
   side=i-1
   for j in range(1,5):
       val+=side
       tot+=val
print tot
       
