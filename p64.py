#!/usr/bin/python
from math import *
from itertools import takewhile

#given some value you want to find the square root of, what is its continued fraction periodicitiy
def periodfract_sqrt(num):
    maxlen=600 #some maximum possible period
    base=int(sqrt(num)) #non repeating base
    frac=list()#repeating fraction
    #convert x/(sqrt(num)-b) to a+(sqrt(num)-new_b)/new_x
    x=1 #numerator    
    b=base #subractor
    while len(frac)<maxlen:
        frac.append(int(x/((sqrt(num)-b))))
        x=(num-b**2)/x
        b=frac[-1]*x-b
    
    #check for repitition in frac
    check=len(set(frac))
    if check==1:
        return 1
    for i in range(2,maxlen,2):
        half=i/2
        if frac[:half]==frac[half:i]:
            if len(set(frac[:half]))==check:
                return half
    print num,frac
    print "Error... your algo sucks!"
    exit(0)


cnt=0
for i in range(2,10001):
    if int(sqrt(i))==sqrt(i):
        continue
    L=periodfract_sqrt(i)
    if L%2==1:
        cnt+=1

print cnt

