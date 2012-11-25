#!/usr/bin/python
from math import *

nums=list()
for a in range(2,101):
    for b in range(2,101):
        t=a**b
        if not(t in nums):
            nums.append(t)
print len(nums)
