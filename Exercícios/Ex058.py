# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar.mostrando no final quantos palpites foram necessários para vencer.
import random

player = 0 
tent = 0 
pc = random.randint(1,10)

while pc != player:
    
    player = int(input("Digite um número inteiro"))
    if player != pc:
        print ("Tente novamente")
        tent += 1

print (f"Voce acertou, o número é {pc}")  
print (f"Foram necessárias {tent} tentativas")   
   