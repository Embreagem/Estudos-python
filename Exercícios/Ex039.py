"""Faça um programa que leia o ano de nascimento de um jovem a informa. de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""


import datetime

nasc = int(input("Qual o ano em que você nasceu? "))

#obter ano atual
data_atual = datetime.datetime.now().year


idade = data_atual - nasc

if idade < 18:
    diff = 18 - idade
    print (f"Ainda falta {diff} anos para se alistar")
elif idade == 18:
    print ("Voce ja pode se alistar")
elif idade > 18:
    diff = idade - 18
    print (f"Ja se passou {diff} anos do alistamento")
   