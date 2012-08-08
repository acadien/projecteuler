#!/usr/bin/python
from math import *

def convert(card):
    if card=="A":
        return 14
    elif card=="K":
        return 13
    elif card=="Q":
        return 12
    elif card=="J":
        return 11
    elif card=="T":
        return 10
    else:
        return int(card)

def gethandval(hand):
    flush=0
    straight=0
    if len(set([i[1] for i in hand]))==1:
        flush=1

    cards=[convert(i[0]) for i in hand]
    diffcards=len(set(cards))
    
    if diffcards==5:
        if max(cards)-min(cards)==4:
            straight=1

    #Straight flush
    if straight==1 and flush==1:
        return [0,max(cards)] #straight/royal flush: 0,high card

    
    if diffcards==2:
        #4 of a kind
        if len([i for i in cards if i==cards[0]])==1:
            return [1,cards[1],cards[0]] # 4 of a kind: 1,major card, minor card
        if len([i for i in cards if i==cards[0]])==4:            
            return [1,cards[0],[i for i in cards if cards[0]!=i][0]] # 4 of a kind: 1,major card, minor card

        #Full House
        if len([i for i in cards if i==cards[0]])==2:
            return [2,[i for i in cards if cards[0]!=i][0],cards[0]] # Full house: 1,major card, minor card        
        else:
            return [2,cards[0],[i for i in cards if cards[0]!=i][0]] # Full house: 1,major card, minor card        
    
    if flush==1:
        #Flush
        return [3]+sorted(cards,reverse=True) #flush with [3,sorted cards]

    if straight==1:
        #Straight
        return [4,max(cards)] #straight with [4,maxcard]

    if diffcards==3 or diffcards==4:
        cnt=list()
        for j in range(5):
            cnt.append(len([i for i in cards if i==cards[j]]))
        #3 of a kind
        if max(cnt)==3:
            maj=cards[cnt.index(max(cnt))]
            cards.remove(maj)
            cards.remove(maj)
            cards.remove(maj)
            return[5,maj]+sorted(cards,reverse=True) #[5,majcard,large minor, small minor]
        if max(cnt)==2:
            major=cards[cnt.index(max(cnt))]
            cards.remove(major)
            cards.remove(major)
            cnt=list()
            for j in range(3):
                cnt.append(len([i for i in cards if i==cards[j]]))
            #2 pair
            if 2 in cnt:
                minor=cards[cnt.index(max(cnt))]
                cards.remove(minor)
                cards.remove(minor)
                return [6,max([major,minor]),min([major,minor]),cards[0]] #[6,major,minor,highcard]
            else:
                #1 pair
                return [7,major]+sorted(cards,reverse=True) #[7,major,highcards]

    #highcard
    return [8]+sorted(cards,reverse=True)

def compare(a,b):
    if a[0]!=b[0]:
        return a[0]<b[0]

    v=a[0]
    a=a[1:]
    b=b[1:]

    # cant both be royal flush
    
    #if both are straight flush:
    if v==0:
        #print "straight flush tie!"
        return a[0]>b[0]

    #if both are four of a kind:
    if v==1:
        #print "4 of a kind tie!"
        if a[0]!=b[0]:
            return a[0]>b[0]
        return a[1]>b[1]

    #if both are fullhouse:
    if v==2:
        #print a,b,"full house tie!"
        if a[0]!=b[0]:
            return a[0]>b[0]
        return a[1]>b[1]

    #if both are flush:
    if v==3:
        #print "flush tie!"
        for i in range(5):
            if a[i]!=b[i]:
                return a[i]>b[i]
        print "Identical hands!"
        return 0 #identical hands 
    
    #if both are straight:
    if v==4:
        #print "straight tie!"
        return a[0]>b[0]
            
    #if both are 3 of a kind:
    if v==5:
        #print "3 of a kind tie!"
        return a[0]>b[0]

    #if both are 2 pair,1 pair or highcard:
    if v==6:
        print "2 pair tie!"
        for i in range(3):
            if a[i]!=b[i]:
                return a[i]>b[i]

    if v==7:
        print "1 pair tie!"
        for i in range(4):
            if a[i]!=b[i]:
                return a[i]>b[i]

    if v==8:
        print "High card tie!"
        for i in range(5):
            if a[i]!=b[i]:
                return a[i]>b[i]
        
poker = open("poker.txt","r")

b=5
a=6
print (a>b)==0

wins1=0
for i,line in enumerate(poker):
    cards=line.split()
    hand1=cards[0:5]
    hand2=cards[5:10]
    val1=gethandval(hand1)
    val2=gethandval(hand2)
    #print val1,val2,compare(val1,val2)
    if compare(val1,val2):
        wins1+=1

print wins1

        
