#!/usr/bin/python
#mine
from PEutil import *
        
largest=0
for i in range(1000,900,-1):
    for j in range(1000,900,-1):
        if palindrome(i*j):
            print i*j,i,j
            exit(0)
