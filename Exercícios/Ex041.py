"""A Confederação Nacional de Natação precisa de um programa que laia o ano de nascimento de um atleta e mostre sua categoria, da acordo com a idade:

Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 20 anos: SENIOR
Acima: MASTER"""
import datetime
nasc = int(input("Qual o ano em que você nasceu? "))

data_atual = datetime.datetime.now().year
idade = data_atual - nasc

if idade <= 9:
    print ("Sua categoria é mirim")
elif idade > 9 and idade <= 14:
    print ("Sua categoria é infantil")
elif idade > 14 and idade <= 19:
    print ("Sua categoria é junior")
elif idade >= 19 and idade <= 20:
    print ("Sua categoria é senior")
elif idade > 20:
    print("Sua categoria é master")    
        
            
                    