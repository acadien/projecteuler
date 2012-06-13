#!/usr/bin/python
from math import *
import sys

def ascii(letter):
    return ord(letter)-64

def cntword(word):
    return sum([ascii(i) for i in word])

def trival(n):
    a=int(sqrt(2*n))
    if a*(a+1)/2==n:
        return True
    return False

fp = open("words.txt")
tot=0
for words in fp:
    words=words.split(",")
    for word in words:
        if trival(cntword(word[1:-1])):
            tot+=1

print tot


