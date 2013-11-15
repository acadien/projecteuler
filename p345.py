#!/usr/bin/python

#p345
#simple monte carlo solver works about 70% of the time.

import pylab as pl
from numpy import *
from random import randint,random

data="7  53 183 439 863 497 383 563  79 973 287  63 343 169 583\n627 343 773 959 943 767 473 103 699 303 957 703 583 639 913\n447 283 463  29  23 487 463 993 119 883 327 493 423 159 743\n217 623   3 399 853 407 103 983  89 463 290 516 212 462 350\n960 376 682 962 300 780 486 502 912 800 250 346 172 812 350\n870 456 192 162 593 473 915  45 989 873 823 965 425 329 803\n973 965 905 919 133 673 665 235 509 613 673 815 165 992 326\n322 148 972 962 286 255 941 541 265 323 925 281 601  95 973\n445 721  11 525 473  65 511 164 138 672  18 428 154 448 848\n414 456 310 312 798 104 566 520 302 248 694 976 430 392 198\n184 829 373 181 631 101 969 613 840 740 778 458 284 760 390\n821 461 843 513  17 901 711 993 293 157 274  94 192 156 574\n 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699\n815 559 813 459 522 788 168 586 966 232 308 833 251 631 107\n813 883 451 509 615  77 281 613 459 205 380 274 302  35 805"

data=array(map(lambda x:map(int,x.split()),data.split("\n")))
i_s = range(0,15)
def matsum(locs):
    return sum([data[i][j] for i,j in zip(i_s,locs)])

def swap(i,j,locs):
    a=list(locs)
    a[i],a[j]=a[j],a[i]
    return a

locs = range(0,15)
val = matsum(locs)

keptvs=[val]
allvs=[val]
N=30000
avg=0
T=30
maxval=val
for i in range(N):
    
    if i==N/3:
        T/=3

    index1 = randint(0,14)
    index2 = randint(0,14)
    
    newlocs = swap(index1,index2,locs)
    newval = matsum(newlocs)
    allvs.append(newval)

    if newval>val:
        maxval=newval
        print i,maxval
        val=newval
        locs=newlocs
        keptvs.append(newval)
    elif exp((newval-val)/T)>random():
        val=newval
        locs=newlocs
        keptvs.append(newval)

print maxval

