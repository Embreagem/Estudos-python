"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa. Calcula seu IMC e mostre seu status. de acordo com a tabela abaixo:

Abaixo de 18.5: Abaixo do Peso
Entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso 
30 até 40: Obesidade
Acima de 40: Obesidade mórbida"""

peso = float(input("Qual o seu peso? "))
alt = float(input("Qual a sua altura? "))
imc = peso / (alt*2)

print (f"Seu imc é de: {imc:.2f}")
if imc < 18.5:
    print ("Você está abaixo do peso!")
elif imc >= 18.5 and imc < 25:
    print ("Você esta no peso ideal")
elif imc >= 25 and imc < 30:
    print ("Você esta com sobrepeso!")
elif imc >= 30 and imc < 40:
    print ("Você esta com obesidade")
elif imc > 40:
    print ("Obesidade morbida! se cuide!")



