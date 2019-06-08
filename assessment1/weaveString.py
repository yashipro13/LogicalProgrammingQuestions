# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 18:02:32 2019

@author: yashi
"""

def weaveString (string1, string2):
    small = len(string1)
    big_string = string2
    output_string = ""
    if len(string2) < small:
        small = len(string2)
        big_string = string2
    for i in range(small):
        output_string = output_string + string1[i] + string2[i]
    output_string += big_string[small:] 
    return output_string

print(weaveString("Yashi","Rocket"))

