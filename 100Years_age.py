# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:07:45 2021

@author: hp
"""

#Program that ask the user to enter their name and age. Print out a message
#addressed to them that tells them the year that they will turn 100 year old.
name= input("Enter your name : ")
age=int(input("Enter your age : "))
year= int(input("Enter the current year : "))
t= 100-age
if t>=100:
    print("You already crossed 100 years")
else:
    ans= year+t
    print("In year",ans,"you will turn 100 years old.")