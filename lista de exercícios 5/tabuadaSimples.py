# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 17:12:26 2023

@author: brend
"""

#tabuada simples

l = 1
c = 1

while c <= 10:
    while l <= 10:
        print(c * l, end = "\t")
        l += 1
    c += 1
    print()
    l = 1
    