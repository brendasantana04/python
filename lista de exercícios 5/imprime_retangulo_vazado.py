# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 15:30:22 2023

@author: brenda

Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres
que não estiverem na borda do retângulo sejam espaços.
"""

def ret(a, l):
    i = 0
    while i < a:
       j = 0
       while j < l:
           if i == 0 or i == a - 1 or j == 0 or j == l - 1:
               print("#", end = "")
           else:
               print(" ", end = "")
           j += 1
       print()
       i += 1

l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

ret(a, l)

    
    