# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 13:49:55 2020

@author: Mert Barbaros
"""

"""
In computing, regex provides a concise and flexible means for matching strings
of text, such as particular charachters, words, or patterns of charachters.
Regular expression is written in a formal language that can be interpreted 
by regular expression processor.

It's a "wild card" expression for matching and parsing strings.

- Very powerful and quite encryptic
- Fun
- Regular expressions are language into themselves


^ beginning of the line
$ end of the line
. Matches any charachter
\s Matches whitespace
\S Matches and non-whitespace charachter 
* Repeats a charachter zero or more times
*? Repeats a charachter zero or more times (non-greedy)
+ Repeats a chrachter one or more times
+? Repeats a charachter one or more times (non-greedy)
[aeiou] Mathces a single chrachter in the listed set
[^XYZ] Matches a single charachter not-in the listed set
[a-z0-9] The set of characters include in a range
( Indicates where the string extraction is start
) Indicates where the string extraction is end

 Before you use it in python, you should import it 
 
 re.search() --> string matches a regex
 re.findall() --> extract portion of string that match your reges
 
 both are like find() in strings
"""

import re

hand = open('mbox-short.txt')

#without regex
for lin in hand:
    lin = lin.rstrip()
    if lin.startswith('From: ') >= 0:
        #lin.find('From: ')
        print(lin)

#with regex

for line in hand:
    line = line.rstrip()
    if re.search('^From: ',line):
        print(line)

#Example

import re 
    
sen_arr = ['X-908', 'Y-E8W87', 'X-6878575', 'Y-KSFLKHS']

for i in sen_arr:
    if re.search('^X-\S+', i):
        print(i)

#re.search() is used for True or False
# re.findall() is used for extracting data 
        
import re

x = 'I developed 1 mobile application that used by 45 people in USA'

y = re.findall('[0-9]+', x)
print(y)

#Greedy and non-greedy
import re

#non-greedy
x = 'From: info@barbaros.blog Hello Dear, How are you?'
y = re.findall('^F.+?:',x)
#: defined the last charachter
print(y)
z = re.findall('\S+@+\S+', x)
print(z)

#with dual split

words = x.split()
email =  words[1]
pieces = email.split('@')
print(pieces[1])

#with regex
# ([^ ]*) means everything starts with a non-white space charachter
t = re.findall('@([^ ]*)',x)
print(t)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
