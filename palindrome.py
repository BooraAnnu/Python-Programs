# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:52:59 2021

@author: hp
"""


def is_Palindrome(string):
    return string == string[::-1]

inputstring=input("Enter a string : ")
result= is_Palindrome(inputstring)

if result:
    print(inputstring,"is palindrome")
    
else:
    print("Not a palindrome")