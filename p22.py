#!/usr/bin/python
from math import *

fp=open("names.txt","r")

for line in fp:
    names=line.split(",")
fp.close()

tot=0

names.sort()
for (i,name) in enumerate(names):
    name=name.rstrip('\"')
    name=name.lstrip('\"')
    loctot=0
    for letter in name:
        loctot+=ord(letter)-64
    tot+=(loctot*(i+1))

print tot
