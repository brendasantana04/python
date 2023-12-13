# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 13:25:54 2023

@author: brenda

Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros
verifica se tal lista possui elementos repetidos e os remove.
A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos.
A lista devolvida deve estar ordenada.

Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?
"""
        
def remove_repetidos(lista):
    lista_sem_repeticao = sorted(list(set(lista)))
    return lista_sem_repeticao

lista = [2, 4, 2, 2, 3, 3, 1]

remove_repetidos(lista)

