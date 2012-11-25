#!/usr/bin/python
from math import *
from itertools import combinations
import string

def decrypt(message,key):
    return ''.join([chr(message[i] ^ key[i%3]) for i in range(len(message))])
        
    

cipher=open("cipher1.txt",'r')
mesg=[int(i) for i in cipher.read().rstrip().split(',')]

words=["the","of","to","and","a","is","in","it"]

chars=string.lowercase*3
encs=combinations(chars,3)
encs=[[ord(j) for j in i] for i in encs]

chars=set(string.printable)

for ky in encs:
    dmesg=decrypt(mesg,ky)
    vals=set(dmesg)
    if vals<=chars:
        if words[0] in dmesg:
            if '.'==dmesg[-1] and '('==dmesg[0]:
                print dmesg
                print sum([ord(i) for i in dmesg])
                    

    



