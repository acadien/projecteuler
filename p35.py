#!/usr/bin/python
from math import *

def check_prime(x,primes):
    sqt=int(sqrt(x))
    for i in primes:
        if x%i==0:
            return False
        if i>sqt:
            break
    return True

def circ(x):
    return x[1:]+x[0]

primes=list()
primes.append(2)
for i in range(3,1000000,2):
    if check_prime(i,primes):
        primes.append(i)

newprimes=list(primes)

tot=0
for i in primes:
    val=str(i)
    if len(val)>1:
        try: 
            list(val).index("0")
            continue
        except ValueError:
            pass
        try: 
            list(val).index("2")
            continue
        except ValueError:
            pass
        try: 
            list(val).index("4")
            continue
        except ValueError:
            pass
        try: 
            list(val).index("5")
            continue
        except ValueError:
            pass
        try: 
            list(val).index("6")
            continue
        except ValueError:
            pass
        try: 
            list(val).index("8")
            continue
        except ValueError:
            pass
    fnd=True
    for j in range(len(val)):
        if not(int(val) in newprimes):
            fnd=False
            break
        val=circ(val)
            
    if fnd:
        tot+=1
        print tot,i
        #newprimes.pop(0)
    exit
print tot
