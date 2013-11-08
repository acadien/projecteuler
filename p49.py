#!/usr/bin/python
from math import *
from itertools import permutations
#mine
from PEutil import *

primes=[i for i in primesfrom2to(10000) if i>999]

for init in primes:
    perms=[''.join(i) for i in permutations(str(init))]
    for adder in range(1000,4000):
        mid=init+adder
        fin=init+adder*2
        if mid>9999 or fin>9999:
            break
        if str(mid) in perms:
            if str(fin) in perms:
                if mid in primes:
                    if fin in primes:
                        print init,init+adder,init+adder*2,adder
                        break
