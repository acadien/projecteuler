#!/usr/bin/python

def check_prime(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

magicval=600851475143
currval=600851475143
largeprime=0
i=2
print check_prime(6857)

while(True):
    if(check_prime(i)):
        if(currval%i==0):
            currval/=i
            largeprime=i
            print i
    i+=1
    if(i>=currval):
        break
    
print i
