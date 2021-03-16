# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:13:22 2021

@author: hp
"""


"""lst1= [int(x) for x in input("Enter list elements : ").split(',')]
lst2=[]
for i in lst1:
    if i % 2==0:
        lst2.append(i)
    
    else:
        break
    
print("New list is : ",lst2)"""
        
#Program that take a list and print a new_list with the even elements of that list only.

def list_with_even(lst):
    final_list=[]
    for i in lst:
        if i % 2==0:
            final_list.append(i)
    
    return final_list

lst= [int(x) for x in input("Enter list elements : ").split(',')]
print(list_with_even(lst))
        