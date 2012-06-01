#!/usr/bin/python
from math import *
import operator
import itertools

primes=list([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97])
sets_primes=map(set,itertools.combinations(primes,4))
sets_products=map(lambda x: reduce(operator.mul,x),sets_primes)
sets_length=len(sets_primes)

maxnum=10**16

def flatten(listOfLists):
    "Flatten one level of nesting"
    return itertools.chain.from_iterable(listOfLists)

total=0
#print maxnum/sets_products[0]
for i in range(0,sets_length):
    print i,total

    current_set=sets_primes[i]
    current_product=sets_products[i]

    current_multiple=maxnum/current_product

    #total+=current_multiple
    done=set()
    for j in range(i+1,sets_length):
        overlap=0
        diff = list( sets_primes[j]-current_set)
        #ndiff=len(diff)
        #if ndiff<4 and ndiff>0:
        #    common_muls=flatten([map(lambda x:reduce(operator.mul,x),itertools.combinations(diff,k)) for k in range(1,ndiff+1)])
        done |= set(diff)
        

        """
        if ndiff==4:
            done.add( sets_products[j])
        elif ndiff>0:
            #common_muls=flatten([map(lambda x:reduce(operator.mul,x),itertools.combinations(diff,k)) for k in range(1,ndiff+1)])
            common_muls=diff
            #if sets_primes[j]==set([3,11,13,17]):
            #    print [i for i in common_muls],current_set
            #    exit(0)
            done |= set(common_muls)
        """
    #print sorted(list(done))[:100]
    #print current_set
    overlap=sum(map(lambda x:current_multiple/x,done))
    #print current_multiple,overlap,current_multiple-overlap
    total+=overlap

    #break
print "Total =",total

