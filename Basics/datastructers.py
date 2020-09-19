# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



"""
Types
"""

sen = 'Hellow World'
print(type(sen))
print(type(5))
print(type(8.0))

"""
Mass/Body Index Calculator
"""

height = input('What is your height in meter?')
height = float(height)
weight = input("What is your weight in kilogram?")
weight = float(weight)

mb_index = (weight / (height * height))

print("Your mass body index is", round(mb_index,2))


"""
Notes
1.A collection allows us to put many values into a single variable
2.Mutable means changable
3.Immutable means not changable
4.Strings are immutable
5.Lists are mutable



"""


friends = ['mert', 'anil', 'hilal']

"""
Counted loop
"""
for i in range(len(friends)):
    friend = friends[i]
    print('Happy new year', friend)
    
"""
Uncounted Loop with a list
"""
    
for friend in friends:
    print("new happ new year", friend)


"""
Lists are mutable
"""

friends[2] = 'kateryna'
print(friends)

"""
Like concatenate strings, we can concatenate lists
"""

a = [ 1,2,3,4,5]
b = [6,7,8,9]
print(a+b)

"""
Slicing: up to but not including
"""

print(a[1:3])

"""
Building list from a scratc
"""

stuff = list() #this is constructor
#add element with append method, append always add the object to end of 
#the list

stuff.append('merhaba')
stuff.append('hello')
print(stuff)
print('merhaba' in stuff)
#lists can be sorted

print(stuff.sort())

"""
Some built-in functions
"""

num = [8,9,11,87,99,65,23,16]
print(num)
print(len(num))
print(max(num))
print(min(num))
print(sum(num))
print(sum(num) / len(num))



"""
list average example
"""
"""
avglist = list()

while True:
    inp = input("Enter a number and type done when you done:")
    if inp == 'done' : break 
    value = float(inp)
    avglist.append(value)

print("average is:", sum(avglist) / len(avglist))

"""
"""
Lists and strings
"""

poem = "How happy is the blameless vestal's lot!The world forgetting, by the world forgot. Eternal sunshine of the spotless mind!Each pray r accepted, and each wish resign d; Labour and rest, that equal periods keep; Obedient slumbers that can wake and weep;Desires compos d, affections ever ev n, Tears that delight, and sighs that waft to Heav n "
#split by default find whitespace, you can add delimeter like ; , ! *....
sp = poem.split()
print(sp)
print(len(sp))

for w in sp:
    print(w)

"""
DICTIONARIES
"""

"""
Memory based key value stores
AAssociative arrays in PHP 
dict()
Dictionaries are like bags-no orders 
we index the things we put in dictionary
with a lookup tag
dictionary content is mutable 
"""

purse = dict()
#12 is the value and  monkey is the key(label)
purse['money'] = 12
purse['candy'] = 3
purse['tissue'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

#You can make empty dictinoary using curly braces

jjj = {'chuck' : 1, 'fred': 42}
print(jjj)

#counting with dictinoaries 
#one common use of dictionaries is counting how
#often we see something (frequency)

ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1

#Dictionary tracebacks 
#error to reference a key which is not in the dict

ccc = dict()
print(ccc['mert'])
#we can use the in operator to see if a key is in the dict
'mert' in ccc


"""
when we encounter a new name, we need to add a new
entry in the dict and if the second or later time we
have seen the name, we simply add one to the count 
in the dict under that name
"""

counts =dict()
names = ['csev', 'cwen', 'csev', 'zgian','cwen']

for name in names:
    
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

print(counts)
    
"""
GET METHOD FOR DICTIONARIES
Pattern of checking to see if a key is already in a
dictionary and assuming a default value if the key
is not there is so commont that there is a method
called get() that does this for us

Default value if key does not exist
and no traceback
"""


if name in counts:
    x = counts[name]
else :
    x = 0
    
#name is the key, 0 is the default value 
#
x = counts.get(name, 0)
print(x)

#Same example 
counts =dict()
names = ['csev', 'cwen', 'csev', 'zgian','cwen']

for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)



"""
Dictionaries and files 

General pattern to count the words in a line of text 
is to split the line into words, then loop through
the words and use a dict to track the count of 
each word independently
"""

counts = dict()
print("Enter a line of text: ")
line = input('')

words = line.split()
print('Words :', words)
print('Counting....')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)

#Definitie loops and dictionaries 

"""
Even though dicts are not stored in order, we can
write a for loop that goes through all the entries
in a dictionary- actually it goes through all of
the keys in the dict and looks up the values
"""

#In list we look the values, but in dicts we look
#to the keys

counts = { 'chuck' : 1, 'fred': 42, 'jan': 100 }
for key in counts:
    print(key, counts[key])

#Retrieving lists of keys and values 

jjj = { 'chuck' : 1, 'fred': 42, 'jan': 100 }
#get the keys
#it will give us in the order
print(list(jjj))
print(jjj.keys())
print(jjj.values())
#returns a tuple 
print(jjj.items())

"""
We loop through the key-value pairs in a dict
using two iteration variables

each iteration, the first variable is the key and the
second variable is the corresponding value
for the key
"""

jjj = { 'chuck' : 1, 'fred': 42, 'jan': 100 }
for aaa,bbb in jjj.items():
    print(aaa, bbb)

stuff = dict()
print(stuff.get('candy', -1))


"""
9.4 Write a program to read through the 
mbox-short.txt and figure out who has 
sent the greatest number of mail messages.
 The program looks for 'From ' lines 
 and takes the second word of those 
 lines as the person who sent the mail. 
 The program creates a Python dictionary 
 that maps the sender's mail address to a 
 count of the number of times they appear 
 in the file. After the dictionary is 
 produced, the program reads through 
 the dictionary using a maximum 
 loop to find the most prolific committer.

"""
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


counts = dict()

for line in handle:
    if line.startswith('From '):
        words = line.split()
        words = words[1]
        counts[words]= counts.get(words,0)+1

bigword = None
bigcount = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count 

print(bigword,bigcount)



"""
Another approach for the problem
"""

fname = input("enter file: ")
if len(fname) < 1 : fname = 'clown.text'
hand = open(fname)

di = dict()

for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    
    for w in wds:
        if w in di:
            di[w] = di[w] + 1
        else:
            di[w] = 1
            print('**New**')
        print(w, di[w])
        
        
        

#with get method
    
fname = input("enter file: ")
if len(fname) < 1 : fname = 'clown.text'
hand = open(fname)

di = dict()


for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    
    for w in wds:
        oldcount = di.get(w,0)
        print(w, 'old', oldcount)
        newcount = oldcount + 1
        di[w] = newcount 
        print(w,'new', newcount)
        
print(di)


#for finding the most common word

largest = -1 
theword = None
for k,v in di.items():
    print(k,v)
    
    if v > largest:
        largest = v 
        theword = k

print(largest)





