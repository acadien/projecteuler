#!/usr/bin/python

from math import *
from operator import mul
import itertools
import sys
import pylab as pl
#mine
from helper import factorize

def checkprodsum(a,N):
    if sum(a)==N:
        return True
    return False

def subsetter(k,basis):
    if basis==[2,2]:
        return [[2,2],[4]]
    sset={str(sorted(basis)):basis}
    totry=list([basis])
    while len(totry)>=1:
        cbasis=totry.pop(0)
        for i in range(len(cbasis)):
            
            tbasis=list(cbasis)

            val=tbasis.pop(i)

            prefix_set=tbasis[:i]

            for j in range(i,len(tbasis)):
                val*=tbasis[j]
                newset=prefix_set+[val]+tbasis[j+1:]
                if not sset.has_key(sum(newset)):
                    if sum(newset)<=2*k:
                        sset[str(sorted(newset))]=newset
                        if len(newset)>=1:
                            totry.append(newset)
                    
    sset=sset.values()

    return zip(*sorted([[sum(s),s] for s in sset],key=lambda x:x[0]))[1]


tots=set()
Ns=list()
True_Ns_2_400=[4, 6, 8, 8, 12, 12, 12, 15, 16, 16, 16, 18, 20, 24, 24, 24, 24, 24, 28, 27, 32, 30, 48, 32, 32, 32, 36, 36, 36, 42, 40, 40, 48, 48, 48, 45, 48, 48, 48, 48, 48, 54, 60, 54, 56, 54, 96, 63, 60, 60, 60, 63, 64, 64, 64, 64, 64, 70, 72, 72, 72, 72, 72, 72, 132, 80, 80, 81, 80, 80, 80, 81, 84, 88, 96, 90, 96, 90, 108, 90, 96, 96, 96, 96, 96, 96, 96, 96, 100, 110, 112, 105, 108, 108, 108, 117, 108, 108, 108, 112, 112, 120, 120, 135, 128, 120, 120, 120, 120, 120, 152, 125, 228, 126, 128, 128, 128, 128, 128, 128, 164, 144, 140, 135, 252, 140, 140, 144, 144, 144, 144, 144, 144, 144, 144, 150, 156, 150, 156, 162, 192, 160, 168, 160, 160, 160, 176, 160, 160, 160, 176, 162, 168, 168, 168, 168, 176, 184, 176, 175, 176, 180, 220, 180, 180, 190, 180, 180, 180, 192, 192, 189, 348, 192, 192, 189, 192, 192, 192, 192, 192, 192, 192, 200, 216, 216, 200, 200, 208, 208, 208, 221, 216, 210, 216, 210, 396, 216, 216, 216, 216, 216, 216, 216, 216, 216, 224, 224, 420, 224, 224, 224, 248, 234, 432, 234, 240, 240, 240, 240, 240, 240, 240, 243, 240, 240, 240, 240, 240, 264, 272, 243, 468, 252, 252, 250, 252, 252, 252, 260, 256, 256, 256, 256, 256, 256, 256, 264, 272, 270, 272, 270, 280, 270, 288, 270, 516, 270, 288, 285, 280, 280, 288, 288, 280, 280, 288, 360, 288, 288, 288, 288, 288, 288, 288, 288, 288, 288, 300, 297, 304, 306, 308, 306, 300, 300, 300, 308, 308, 312, 312, 312, 312, 312, 320, 315, 320, 320, 600, 315, 320, 324, 320, 320, 320, 320, 320, 320, 320, 330, 324, 324, 324, 342, 336, 336, 336, 342, 336, 336, 336, 336, 336, 343, 352, 352, 440, 351, 384, 350, 352, 351, 360, 350, 352, 352, 360, 360, 360, 360, 360, 364, 360, 360, 360, 360, 360, 360, 468, 378, 380, 375, 408, 380, 380, 384, 392, 378, 384, 375, 384, 378, 384, 378, 384, 384, 384, 384, 384, 384, 384, 384, 384, 384, 392, 392, 396, 396, 396, 405, 420, 400, 400, 405, 400, 400, 400, 405, 448, 432, 432, 405, 416, 416, 456, 416, 416, 416] #this took 31 seconds to run

def check_Ns(Ns):
    if Ns!=True_Ns_2_400:
        print "You suck."

"""
kndiff=list()
solutions=list()
for k in range(2,400):
    N=k

    while True:
        N+=1
        basefacs=factorize(N)
        if sum(basefacs)+k-len(basefacs)>N:
            continue
        allfacs=subsetter(k,basefacs)
        if len(allfacs)==1:
            continue
            
        #print N,allfacs
        done=False
        for facs in allfacs:

            if len(facs)==1:
                continue
            
            trialset=[1]*(k-len(facs))+facs
            if checkprodsum(trialset,N):
                tots.update([N])
                solutions.append(sum(tots))
                Ns.append(N)
                kndiff.append(N-k)
                print k,N,sorted([i for i in trialset if i!=1])
                done=True
                break
        if done:
            break
print Ns
check_Ns(Ns)
#pl.plot(kndiff)
#pl.plot(sorted(list(set(solutions))))
#pl.show()
"""
