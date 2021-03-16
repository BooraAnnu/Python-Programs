# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:00:08 2021

@author: hp
"""


def divisors(num):
    final_list=[]
    i=1
    while i<num:
        if num % i==0:
            final_list.append(i)
        i+=1
    return final_list
    
num=int(input("Enter a number : "))
print("List of divisors of ",num,"are : ")
print(divisors(num))
