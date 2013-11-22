#!/usr/bin/python

import sys
from numpy import zeros
from operator import mul
from math import factorial

print "usage: ./p172.py #digits #duplicates"
print "Answers the question: How many numbers with D digits have N or fewer duplicates, ignoring numbers with leading 0's"

D= 3
N= 18

Nfac=factorial(N)
dc=zeros([10])
count=0
for dc[0] in range(0,D+1):
    for dc[1] in range(0,D+1):
        for dc[2] in range(0,D+1):
            for dc[3] in range(0,D+1):
                for dc[4] in range(0,D+1):
                    for dc[5] in range(0,D+1):
                        for dc[6] in range(0,D+1):
                            for dc[7] in range(0,D+1):
                                for dc[8] in range(0,D+1):
                                    for dc[9] in range(0,D+1):
                                        if dc.sum()==N:
                                            count += Nfac / reduce(mul,map(factorial,dc))
print count*9/10
