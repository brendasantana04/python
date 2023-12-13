# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 20:18:23 2023

@author: brenda

Escreva um programa que recebe uma sequência de números inteiros e imprima
todos os valores em ordem inversa. A sequência sempre termina pelo número 0.
Note que 0 (ZERO) não deve fazer parte da sequência.


"""

def inverter():
    v = int(input("Digite um número: "))
    lista = []
    
    while v != 0:
        lista.append(v)
        v = int(input("Digite um número: "))
        
    #inverte a lista
    lista.reverse()
    
    for i in range(len(lista)):
        print(lista[i])
    
        

inverter()