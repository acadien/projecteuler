#!/usr/bin/python

def fib(x1,x2):
    return x1+x2

x2=2
x1=1
tot=2
while(x2<4E6):
    x=fib(x1,x2)
    if(x%2==0):
        tot+=x
    x1=x2
    x2=x
print tot
