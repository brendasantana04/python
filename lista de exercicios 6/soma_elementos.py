# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 13:27:09 2023

@author: brenda

Escreva a função soma_elementos que recebe como parâmetro uma lista com números
inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.


"""

def soma_elementos(lista):
    soma = 0
    i = len(lista)
    for i in lista:
        soma = soma + i
    print (soma)
    return soma

lista = [2, 4, 2, 2, 3, 3, 1]

soma_elementos(lista)