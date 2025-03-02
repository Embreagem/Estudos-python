#Faça um programa que leia três números a mostra qual é o maior a qual é o menor.

a = int(input(" Digite o 1° numero "))
b = int(input(" Digite o 2° numero "))
c = int(input(" Digite o 3° numero "))

#Qual o menor?
menor = a
if b <= c and b <= a:
    menor = b
if c <= b and c <= a:
    menor = c
    
print (f" O menor numero é: {menor}")
#Qual o maior?
maior = a 
if b >= c and b >= a:
    maior = b
if c >= b and c >= a:
    maior = c
    
print (f" O maior numero é: {maior}")

