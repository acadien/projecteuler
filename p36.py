#!/usr/bin/python
from math import *
from PEutil import *

tot=0
for i in range(1E6+1):
    if palindrome(i) and palindrome(bin(i)[2:]):
        tot+=i
print tot

