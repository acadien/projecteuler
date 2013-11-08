#!/usr/bin/python
from gmpy import is_square
import sys
M=int(sys.argv[1])
powers=range(int(((M+M)**2+M**2)**0.5)+1)

count=0
for i in range(1,M+1):
    for j in range(i,M+1):
        a=(i+j)**2
        count+=sum([1 for k in range(j,M+1) if is_square(a+k**2)])
        print count
print count
