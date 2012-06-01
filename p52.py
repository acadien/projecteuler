#!/usr/bin/python

def cmpdig(a,b):
    for diga in a:
        if b.count(diga)==0:
            return False
        else:
            i=b.index(diga)
            c=b[0:i]+b[i+1:]
            b=c
    if b=="":
        return True
    return False
            


n=100000

while True:
    n+=1
    if cmpdig(str(n),str(n*2)):
        if cmpdig(str(n),str(n*3)):
            if cmpdig(str(n),str(n*4)):
                if cmpdig(str(n),str(n*5)):
                    if cmpdig(str(n),str(n*6)):
                        break
    if n%10000==0:
        print n
        
print n
