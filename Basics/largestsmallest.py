# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:31:12 2020

@author: Mert Barbaros
"""

"""
Write a program that repeatedly prompts a user for integer numbers until 
the user enters 'done'. Once 'done' is entered, print out the largest and 
smallest of the numbers. If the user enters anything other than a valid number
catch it with a try/except and put out an appropriate message and ignore 
the number. Enter 7, 2, bob, 10, and 4 and match the output below.

Invalid input
Maximum is 10
Minimum is 2
"""

#Assign largest and smalles value as a None. 
largest = None
smallest = None

while True:
    
    num = input("Enter a number: ")
    #skip the while when user input is "done"
    if num == "done":
        break
    #Invalid message for the non int inputs except "done" 
    try:
        fnum = int(num)
    except:
        print("Invalid input")
        #back to top of the loop
        continue
    
    if largest is None or largest < fnum:
        largest = fnum
        
    if smallest is None or smallest > fnum:
        smallest = fnum
        
print("Maximum is ",largest)
print("Minimum is ",smallest)        
