#!/usr/bin/python

#By Adam & Victoir Jan/2012

from itertools import *
from numpy import array,dot
from scipy import sparse

def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)

def makedist(permset):
    return [sum(permset[0:i+1]) for i in range(len(permset)-1)]

def checkcrack(a,b):
    combo=a+b
    if len(combo)==len(set(combo)):
        return 1
    return 0

width=32
height=10

#The basis sets for the 6 different kinds of walls
base2=[[2],[2]*4,[2]*7,[2]*10,[2]*13]
base3=[[3]*10,[3]*8,[3]*6,[3]*4,[3]*2]

#Calculate every permutation of base2[i]+base3[i]
permsets=list()
for l in range(len(base2)):
    a=base2[l]
    b=base3[l]
    ms=[b]
    while len(a)>0:
        insertme=a.pop()
        newms=list()
        for m in ms:
            pp=list(m)
            newms += [tuple(pp[:i]+[insertme]+pp[i:]) for i in range(len(pp)+1)]
        ms=list(set(newms))
    permsets+=ms
permsets.append(tuple([2]*16))

#Represent the walls by a list of the length at the end of each block in the wall
walls = [makedist(i) for i in permsets]
N=len(walls)

#Generate the connectivity matrix that represents if each wall can be stacked on each other wall without a crack
connects=array([array([checkcrack(walls[i],walls[j]) for j in range(N)]) for i in range(N)])

#Use sparse matrices for fast matrix multiplication
connects=sparse.dok_matrix(connects)

#Multiply the connectivity matrix by itself to gather the total number of combinations, do this for each layer
tot=sparse.dok_matrix(connects)
for i in range(height-2):
    tot=connects.dot(tot)
    print "hooray"

#holy fuck, it works.
print tot.sum()


