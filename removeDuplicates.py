# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:32:06 2021

@author: hp
"""


#To remove duplicates from the list and return a new list of te elements without any duplicate.

def removeDuplicates(lst):
    final_list=[]    #take a empty list
    for i in lst:
        if i not in final_list:
            final_list.append(i)
    
    return final_list

lst= [int(x) for x in input("Enter a list : ").split(",")]
print(removeDuplicates(lst))