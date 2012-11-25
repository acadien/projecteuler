#!/usr/bin/python
from math import *
from itertools import combinations as perms

#Start by generating the list of all 4 digit tri/squ/pen/hx/hep/oc numbers.
def tri(n):
    return n*(n+1)/2

def squ(n):
    return n*n

def pen(n):
    return n*(3*n-1)/2

def hx(n):
    return n*(2*n-1)

def hep(n):
    return n*(5*n-3)/2

def oc(n):
    return n*(3*n-2)

tris=list()
i=1
while True: 
    a=tri(i)
    if a>9999:
        break
    if a>999:
        tris.append(a)
    i=i+1

squs=list()
i=1
while True: 
    a=squ(i)
    if a>9999:
        break
    if a>999:
        squs.append(a)
    i=i+1

pens=list()
i=1
while True: 
    a=pen(i)
    if a>9999:
        break
    if a>999:
        pens.append(a)
    i=i+1

hexs=list()
i=1
while True: 
    a=hx(i)
    if a>9999:
        break
    if a>999:
        hexs.append(a)
    i=i+1

heps=list()
i=1
while True: 
    a=hep(i)
    if a>9999:
        break
    if a>999:
        heps.append(a)
    i=i+1

octs=list()
i=1
while True: 
    a=oc(i)
    if a>9999:
        break
    if a>999:
        octs.append(a)
    i=i+1

#Tells you which sets a number is in
def findset(a):
    sets=[]
    if a in tris:
        sets.append(3)
    if a in squs:
        sets.append(4)
    if a in pens:
        sets.append(5)
    if a in hexs:
        sets.append(6)
    if a in heps:
        sets.append(7)
    if a in octs:
        sets.append(8)
    return sets

#Tells you if each number in list 'nums' is from a different polygonal set
def isuniq(a,b,c,d,e,f):
    an=findset(a)
    bn=findset(b)
    cn=findset(c)
    dn=findset(d)
    en=findset(e)
    fn=findset(f)
    for a in an:
        for b in bn:
            for c in cn:
                for d in dn:
                    for e in en:
                        for f in fn:
                            if len(set([a,b,c,d,e,f]))==6:
                                return True
    return False


#Returns True if the two 4-digit numbers (a,b) are cyclic
def iscyc(a,b):
    ast=str(a)
    bst=str(b)
    if ast[2:4]==bst[0:2]:
        return True
    return False

#Run over each one of these numbers
cycs=set(tris+squs+pens+hexs+heps+octs)

for a in cycs:
    for b in cycs:
        if iscyc(a,b):
            for c in cycs:
                if iscyc(b,c):
                    for d in cycs:
                        if iscyc(c,d):
                            for e in cycs:
                                if iscyc(d,e):
                                    for f in cycs:
                                        if iscyc(e,f) and iscyc(f,a):
                                            if isuniq(a,b,c,d,e,f):
                                                print "Win!"
                                                print a,b,c,d,e,f
                                                print a+b+c+d+e+f
                                                exit(0)

