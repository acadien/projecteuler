#!/usr/bin/python
from math import *

#How to calculate ccrolls and pprolls
"""
#PP: 9 x 4 sided dice
psides=4
pprolls=[0]*37
for r1 in range(1,5):
    for r2 in range(1,5):
        for r3 in range(1,5):
            for r4 in range(1,5):
                for r5 in range(1,5):
                    for r6 in range(1,5):
                        for r7 in range(1,5):
                            for r8 in range(1,5):
                                for r9 in range(1,5):
                                    s=r1+r2+r3+r4+r5+r6+r7+r8+r9
                                    pprolls[s]+=1
#CC: 6 x 6 sided dice
csides=6
ccrolls=[0]*37
for r1 in range(1,7):
    for r2 in range(1,7):
        for r3 in range(1,7):
            for r4 in range(1,7):
                for r5 in range(1,7):
                    for r6 in range(1,7):
                        s=r1+r2+r3+r4+r5+r6
                        ccrolls[s]+=1
"""
pprolls=[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 45, 165, 486, 1206, 2598, 4950, 8451, 13051, 18351, 23607, 27876, 30276, 30276, 27876, 23607, 18351, 13051, 8451, 4950, 2598, 1206, 486, 165, 45, 9, 1]
npprolls=sum(pprolls)

ccrolls=[0, 0, 0, 0, 0, 0, 1, 6, 21, 56, 126, 252, 456, 756, 1161, 1666, 2247, 2856, 3431, 3906, 4221, 4332, 4221, 3906, 3431, 2856, 2247, 1666, 1161, 756, 456, 252, 126, 56, 21, 6, 1]
nccrolls=sum(ccrolls)

#Normalize
ccrolls=[float(i)/nccrolls for i in ccrolls]
pprolls=[float(i)/npprolls for i in pprolls]

#loop over all of prolls possible rolls, find the odds of him winning that one, weight it
t=0
for proll in range(37):
    prob_proll=pprolls[proll]
    for croll in range(proll):
        t+=prob_proll*ccrolls[croll]
print round(t,7)

