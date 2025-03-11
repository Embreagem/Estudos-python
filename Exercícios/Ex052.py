"""Faça um programa que leia um número inteiro a diga sa ala é OU NÃO Um número primo."""

tot = 0
num = int(input("Digite um numero"))

for c in range(1, num +1):
    if num % c == 0:
        tot += 1

if tot == 2:
    print (f"{num} é primo)
else:
    print (f"{num} não é primo")



        