#!/usr/bin/python
from math import *
#mine
from PEutil import *

RANGE_MIN=0
RANGE_MAX=1000

n=1000
bigN=5E10
primes=[i for i in primesfrom2to(n).tolist() if i<RANGE_MAX and i>RANGE_MIN]

bigs=list()
for D in primes:
    x1=1
    x2=-1
    fnd=False
    D=float(D)
    while x1<bigN:
        x1+=D
        x2+=D
        a1=((x1**2-1)/D)**0.5
        a2=((x2**2-1)/D)**0.5
        if a1==int(a1):
            print "D=%d, X=%d, Y=%d"%(D,x1,a1)
            fnd=True
            break
        if a2==int(a2):
            print "D=%d, X=%d, Y=%d"%(D,x2,a2)
            fnd=True
            break
        
    if fnd==False:
        print "D=%d is >%d"%(D,bigN)
        bigs.append([D,X])

print bigs

""" 0-500
NADA
"""

""" 500-600
D=521, X=16204035717, Y=709911694
D=571, X=14418553398, Y=603397680
"""

""" 600-700
D=617, X=13049185969, Y=525340446
"""

""" 700-800
D=739, X=10548978175, Y=388050435
D=757, X=16349010755, Y=594214903
D=787, X=15441236698, Y=550420644
"""

""" 800-900
D=809, X=11620158062, Y=408543001
D=853, X=10652273384, Y=364726894
D=859, X=12080759531, Y=412190196
D=863, X=10419508171, Y=354684183
D=883, X=17301967340, Y=582257560
"""

"""900-1000
D=907, X=15285382575, Y=507542798
D=919, X=16445222866, Y=542477847
D=947, X=13509645362, Y=439004487
D=953, X=16910620002, Y=547788714
D=971, X=16515496251, Y=530007497
D=977, X=14340446056, Y=458791516
D=991, X=20459665726, Y=649922701
D=997, X=10300130629, Y=326208410

"""
