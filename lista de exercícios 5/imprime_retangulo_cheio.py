# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 15:30:22 2023

@author: brenda

Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros
correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir,
usando repetições encaixadas (laços aninhados), uma cadeia de caracteres que represente o retângulo 
informado com caracteres '#' na saída.
"""

l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

aux = l

while a > 0:    
    while l > 0:
        print("#", end="")
        l-= 1
    a -= 1
    l = aux
    print()
    