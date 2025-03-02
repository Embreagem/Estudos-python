#Cria um programa que laia um número inteiro a mostra na tala sa ala é PAR ou IMPAR.

num = int(input("Digite um numero inteiro "))
rest = num % 2
if rest == 0:
    print (f" {num} é par!")
else:
    print (f" {num} é impar!")