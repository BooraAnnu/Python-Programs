# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 09:39:25 2021

@author: hp
"""

# A  program to find the number of elements in a file

count=0
#open file in read mode
file= open("C:\\Users\\hp\\Desktop\\Python-Programs\\data.txt", "r")

for line in file:
    #Split each line into names
    names= line.split(" ")  
    #Count each name
    count += len(names)     
    
print("Numbers of names given in the list are : ",count)

file.close()

