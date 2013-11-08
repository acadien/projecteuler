#!/usr/bin/python
import primes as prms

ofile=open("multiplesTo1MilTest.txt","w")
ofile.write("0\n1\n")
bigN=1000000

primes=prms.primesfrom2to(bigN)

decomposed=[list() for i in range(bigN+1)]
for i in range(2,bigN+1):
    cm=list()
    val=int(i)
    if i in primes:
        cm=[i]
    else:
        for p in primes:
            if i%p==0:
                cm.append(p)
                cm+=decomposed[i/p]
                break

    decomposed[val]=list(cm)

    ofile.write(" ".join(map(str,cm))+"\n")
