#!/usr/bin/python

import sys

print "usage: ./p172.py #digits #duplicates"
print "Answers the question: How many numbers with D digits have N or fewer duplicates, ignoring numbers with leading 0's"

D= int(sys.argv[1])
N= int(sys.argv[2])

start = 10**(D-1)
end = 10**(D)
print start,end-1

digits = map(str,range(10))

def checkDup(val,N):
    sval = str(val)
    if max([sval.count(i) for i in digits]) > N:
        return 0
    return 1

print sum([checkDup(i,N) for i in range(start,end)])
