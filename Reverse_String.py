# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:36:08 2021

@author: hp
"""

def ReverseString(string):
    words= string.split()
    final_string =" ".join(reversed(words))
    return final_string

input= "Hello I am a student."
print(ReverseString(input))
