# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 20:14:33 2023

@author: brenda

Escreva a função maior_elemento que recebe como parâmetro uma lista com números
inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida.


"""

def maior_elemento(lista):
    i = len(lista)
    
    elemento_maior = 0
    
    for i in lista:
        if i > elemento_maior:
            elemento_maior = i
    print(elemento_maior)
    
    return elemento_maior
    
lista = [2, 8, 2, 5, 3, 2, 4]

maior_elemento(lista)

    