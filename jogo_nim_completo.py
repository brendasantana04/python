# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 14:05:05 2023

@author: brenda santana santos - @brendasantana04
"""

selecInv = False

def campeonato():
    placar = {"Computador": 0, "Usuário": 0}
    i = 0
    for _ in range(3):
        i += 1
        print("**** Rodada",i,"****")
        print()
        vencedor = partida()
        if vencedor == "Computador":
            placar["Usuário"] += 1
        else:
            placar["Computador"] += 1
        
    
    print("**** Final do campeonato! ****")
    print("Placar: Você",placar["Usuário"],"X",placar["Computador"],"Computador")
    

def computador_escolhe_jogada(n, m):
    jogada = 1
    
    while jogada <= m:
        if (n - jogada) % (m + 1) == 0:
            return jogada
        jogada += 1
    
    # Se não encontrar uma jogada para deixar múltiplo de (m+1), o computador remove 1 peça
    return 1


def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))

    while jogada <= 0 or jogada > m or jogada > n:
        print()
        print("Oops! Jogada inválida! Tente de novo.")
        print()
        jogada = int(input("Quantas peças você vai tirar? "))
    
    return jogada


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print()
        print("Você começa!")
        print()
        jogador_atual = "Usuário"
    else:
        print()
        print("Computador começa!")
        print()
        jogador_atual = "Computador"

    while n > 0:
        
        if jogador_atual == "Computador":
            jogada = computador_escolhe_jogada(n, m)
            if jogada == 1:
                print("O computador tirou uma peça.")    
            else:
                print("O computador tirou", jogada, "peças.")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            if jogada == 1:
                print("Você tirou uma peça.")    
            else:
                print("Você tirou", jogada,"peças.")
        n -= jogada
        
        
        if n == 1 and n != 0:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        elif n != 0 and n != 1:            
            print("Agora restam",n,"peças no tabuleiro.")
            print()

        if n == 0:
            if jogador_atual == "Computador":
                print("Fim do jogo! O computador ganhou!")
                print()
            else:
                print("Você venceu!")
                print()
            break

        if jogador_atual == "Computador":
            jogador_atual = "Usuário"
        else:
            jogador_atual = "Computador"


def main():
    print()
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    while selecInv == False:
        print("1 - para jogar uma partida isolada")
        print("2 - para jogar um campeonato")
    #input do usuario
        t = int(input())
        if t == 1:
            print("Voce escolheu partida isolada!")
            print()
            selecInv == True
            partida()
            break
        elif t == 2:
            print("Voce escolheu um campeonato!")
            print()
            selecInv == True
            campeonato()

#campeonato() é chamar a partida tres vezes
#funcoes devem devolver o numero de peças removidas, e nao o numero de peças sobrando

main()
