#!/usr/bin/python

def check_trip(a,b,c):
    if a*a+b*b-c*c==0:
        return True
    return False

for i in range(1,1000):
    print i
    for j in range(i,1000):
        for k in range(j,1000):
            if i+j+k==1000:
                if check_trip(i,j,k):
                    print i*j*k,i,j,k
                    exit(0)
