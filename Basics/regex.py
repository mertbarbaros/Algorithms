# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:58:19 2020

@author: Mert Barbaros
"""

#Finding sum in the file
import re

hand = open('regex.txt', 'r')

z = list()

for line in hand:
    sline = line.rstrip()
    #find all the numbers 
    fin = re.findall('[0-9]+', sline)
    #add the return list to empty z list
    z = fin + z
    

summ = 0

for i in z:
    #increase the sum by turn all the strings in the z list to integer
    summ = summ + int(i)

print(summ)
