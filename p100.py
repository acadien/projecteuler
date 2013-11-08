#!/usr/bin/python

for n in range(10000):
    for x in range(n):
        if n*(n-1)*0.5==x*(x-1):
            print x,n,float(x)/n
            break

#The N'th pythagorean triple:1070379110497
