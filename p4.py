#!/usr/bin/python

def check_paldrm(x):
    pal=str(x)
    for i in range(len(pal)/2+1):
        if pal[i]!=pal[-(i+1)]:
            return False
    return True
        
largest=0
for i in range(1000,900,-1):
    for j in range(1000,900,-1):
        if check_paldrm(i*j):
            print i*j,i,j
            exit(0)
