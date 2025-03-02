#Escreva um programa que leia a velocidade de um carro.
#Se ale ultrapassar 80km/h. mostra uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7.00 por cada Km acima do limite.

import sys
limit = 80
speed = float(input("Qual a velocidade? "))
if speed < limit or speed == 80:
    print ("Está tudo bem com a sua velocidade")
    sys.exit()

limit_broken = speed - limit
if speed > limit:
    print (f"Cuidado, passou {int(limit_broken)}km/h acima do permitido")

penalty = limit_broken * 7
print (f"A sua multa sera de: R${penalty:.2f} reais")

