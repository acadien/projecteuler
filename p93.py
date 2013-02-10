#!/usr/bin/python

import operator
import itertools
from itertools import chain
import numpy as np

def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)

operators = [operator.add,operator.div,operator.sub,operator.mul]

#All possible operators
func_evals= [i for i in itertools.product(operators,repeat=3)] 

#All possible digits (not-permuted yet!)
all_combo_digs=itertools.combinations(map(float,range(1,10)),4)


#Evaluation function, handles div by 0, non-integer results and parens
def evaluate(vals,ops):
    a,b,c,d=vals
    op1,op2,op3=ops
    vs=[]

    #5 possible parens ordering
    try :
        s=op3(op2(op1(a,b),c),d)
        vs.append(s)
    except ZeroDivisionError:
        pass

    try :
        s=op2(op1(a,b),op3(c,d))
        vs.append(s)
    except ZeroDivisionError:
        pass

    try :
        s=op3(op1(a,op2(b,c)),d)
        vs.append(s)
    except ZeroDivisionError:
        pass

    try :
        s=op1(a,op3(op2(b,c),d))
        vs.append(s)
    except ZeroDivisionError:
        pass

    try :
        s=op1(a,op2(b,op3(c,d)))
        vs.append(s)
    except ZeroDivisionError:
        pass
    
    #Drop non-integer results!
    return map(lambda x: int(x) if int(x)==x else -1,vs)


#Loop over all digit combos, calculate permutations and count consecutive solutions
consec_run=0
cr_digs=[]
cr_results=[]
for digs in all_combo_digs:
    dig_perms = [i for i in itertools.permutations(digs,4)]

    results = set(flatten([flatten([evaluate(vals,ops) for ops in func_evals]) for vals in dig_perms]))
    
    #results = set(flatten([evaluate(digs,ops) for ops in func_evals]))
    results = sorted([i for i in results if i>0])

    #Get the larges consecutive run starting from the first element
    c=1
    for i in range(len(results)-1):
        if results[i+1]-results[i]==1:
            c+=1
        else: 
            break

    if c>consec_run:
        consec_run=c
        cr_digs=digs
        cr_results=results

print cr_results
print consec_run
print "".join(map(lambda x:str(int(x)),cr_digs))
