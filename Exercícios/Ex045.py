"""Cria um programa que faça o computador jogar Jokanpô com você"""

import random
import sys

print (" Jokanpô \n 1 - Tesoura \n 2 - Pedra \n 3 - Papel")
player_move = str(input("Qual o seu movimento? ")).strip().upper()

if player_move == "TESOURA":
    player = 1
elif player_move == "PEDRA":
    player = 2
elif player_move == "PAPEL":
    player = 3
else:
    print ("Digite um movimento valido!")
    sys.exit()

pc_move= [1, 2 ,3]
pc = random.choice(pc_move)


if (player == 1 and pc == 3) or (player == 2 and pc == 1) or (player == 3 and pc == 2):
    result = "ganhou!"
elif player == pc:
    result = "empatou"
else:
    result = "perdeu!"


if pc == 1:
    pc = "Tesoura"
elif pc == 2:
    pc = "Pedra"
elif pc == 3:
    pc = "Papel"    
    

print (f"Sua jogada foi: {player_move}")
print (f"A minha jogada foi: {pc}")
print (f"Você {result} ")
 
         

                