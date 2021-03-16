# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:46:53 2021

@author: hp
"""
#program that gives a new list of elements that contain the elements which are less than 5.

lst= [int(x) for x in input("Enter list : ").split(",")]   

print("Original list is : ",lst)
for i in lst:
    if i < 5:
        print(i)
    else:
        break
    