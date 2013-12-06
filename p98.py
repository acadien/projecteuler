#!/usr/bin/python


def dict2str(d):
    s=""
    keys=d.keys()
    vals=d.values()
    for k,v in sorted(zip(keys,vals),key=lambda x:x[0]):
        s+=str(k)+str(v)
    return s

words = [word.strip("\"") for word in open("words.txt").readline().split(",")]

#print words
wordletters=list()
annagramWords=dict()
for word in words:
    d1=dict()

    #Break down words into letter counters
    for letter in word:
        try:
            d1[letter]+=1
        except KeyError:
            d1[letter]=1
    wordletters.append(d1)

#Find annagrams
annagramWords=dict()
for i,wl1 in enumerate(wordletters):
    for j,wl2 in enumerate(wordletters[i+1:]):
        if wl1==wl2:
            hd=dict2str(wl1)
            try:
                if words[i+j+1] not in annagramWords[hd]:
                    annagramWords[hd].append(words[i+j+1])
            except:
                annagramWords[hd]=[words[i],words[i+j+1]]

#annagramWords has all of the annagrams... now find all the possible combos of squares
m=0

largestAnnagrams=dict()
for i in annagramWords.items():
    a= max(map(len,i[1]))
    if a>m:
        m=a

squares=list()
m=5
for i in range(100000):
    a=i*i
    l=len(str(a))
    if l<m: continue
    if l>m: break
    if len(set(str(a)))==m:
        squares.append(a)
    
print len(squares),"possible squares no longer than",m,"letters, no solutions for 6-9 lengths"

#squares is all possible square numbers
pwords=list()
for hd1,wds in annagramWords.items():
    if len(wds[0])==m:
        pwords.append(wds)

#Loop over annagram words, create the spindex corresponding to converting one word to the other
#check if the spindex transformation works on the square numbers, if it does then take the max
for pword in pwords:
    spindex=[pword[1].index(l) for l in pword[0]]
    for n in squares:
        sn = str(n)
        v=["0"]*m
        for i in range(m):
            v[spindex[i]]=sn[i]
        iv = int("".join(v))
        if len(str(iv))!=m:
            continue
        if iv in squares:
            print "Solution:",max(n,iv)
