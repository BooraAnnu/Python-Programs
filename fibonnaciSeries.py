# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 08:50:29 2021

@author: hp
"""
# Program to print the fibonnaci series 

n= int(input("Enter how many fibonnaci numbers : "))
f1=0
f2=1
if n<0:
    print("Incorrect input")
elif n==0:
    print(f1)
elif n==1:
    print(f2)
else:
    print(f1,"\n", f2, sep="")
    for i in range(2,n):
        f = f1 + f2
        print(f)
        f1=f2
        f2=f