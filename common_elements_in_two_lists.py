# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:05:53 2021

@author: hp
"""
#List of common elements of two lists of different sizes.
lst1= [int(x) for x in input("Enter first list elements : ").split(",")]
lst2=[int(x) for x in input("Enter second list elements : ").split(",")]

s1= set(lst1)
s2= set(lst2)

s3= s1.intersection(s2)

common_list= list(s3)  #convert set in list
 
print(common_list)