#Escreva um programa que pergunte o salário de um Funcionário a calcula o valor do seu aumento.
#Para salários superiores a R$1.250.00. calcula um aumento de 10%.
#Para os inferiores ou iguais, o aumento é da 15%.
import sys

salario = float(input("Qual o seu salario? "))

if salario >= 1.250:
    aumento = (salario * 0.10) + salario
if salario < 1.250:
    aumento = (salario * 0.15) + salario
print (f"Seu novo salario é de: R${aumento:.2f} reais")
    