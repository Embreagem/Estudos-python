#Desenvolva um programa que laia o comprimento de três ratas a diga ao usuário sa alas podem ou não formar um triângulo.

a = float(input("Comprimento lado A "))
b = float(input("Comprimento lado B "))
c = float(input("Comprimento lado C "))

reta = (a+b > c) and (b+c > a) and (c+a > b)

if reta == True:
    print ("Esse conjunto forma um triangulo")
else:
    print ("Esse conjunto nao forma um triangulo")


