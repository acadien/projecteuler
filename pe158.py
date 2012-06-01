#!/usr/bin/python

import itertools
import sys
from operator import mul


"""
def check1lexo(L):
    #L=list(L)
    if sum(map(lambda a,b:1 if a>b else 0,L[1:],L[:-1]))==1:
        return True
    return False

n=int(sys.argv[1])
l=int(sys.argv[2])
"""
#pnn=2**n-n-1

#alpha=range(l)
#combo=itertools.permutations(alpha,int(n))
#pn=map(check1lexo,combo).count(True)
#print pnn,pn,pn/pnn
#print l*(l-1)*(l-2)*(l-3)/24
#print l*(l-1)*(l-2)*(l-3)*(l-4)/120
#26
#n,      p(n)
#2,       325
#3,     10400
#4,    164450
#5,   1710280


#l,  p(2,l), p(3,l), p(4,l), p(5,l) 
#1   0       0       0       0       
#2   1       0       0       0
#3   3       4       0       0
#4   6       16      11      0 
#5   10      40      55      26 
#6   15      80      165     156 
#7   21      140     385     564
#8   28      224     770     1456

#along the diagonal p(l,l)=2^l - l - 1

#j(n,l)=p(n,l)/p(l,l)
#l,  j(2,l), j(3,l), j(4,l), j(5,l) 
#1   0       0       0       0
#2   1       0       0       0
#3   3       1       0       0
#4   6       4       1       0
#5   10      10      5       1
#6   15      20      15      6
#7   21      35      35      21
#8   28      56      70      56


#j(2,l)=l*(l-1)/2
#j(3,l)=l*(l-1)*(l-2)/6
#j(4,l)=l*(l-1)*(l-2)*(l-3)/24
#j(5,l)=l*(l-1)*(l-2)*(l-3)*(l-4)/120

##################
#The solution
##################
#This function was solved for using the data points generated above.
#No real math necessary!  Just a function of two variables and then 
#reverse engineer the set to get the function...
def p(n,l):
    l+=1
    pnn=2**n-n-1 #euler number
    divis=reduce(mul,range(1,n+1))
    numer=reduce(mul,range(l-n,l))
    return numer/divis*pnn

l=26 #alphabet has 26 characters
ps=list()
for n in range(1,27):
    print n,p(n,l)
    ps.append(p(n,l))
print "Max:",max(ps),ps.index(max(ps))+1
