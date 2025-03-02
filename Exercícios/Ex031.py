# Desenvolva um programa que pergunta a distância de uma viagem em Km. Calcula o preço da passagem.cobrando R$0.50 por Km para viagens de até 200Km a R$0.45 para viagens mais longas.
import sys
km = float(input("Quantos km's? "))
if km >= 200:
    price = km * 0.45
else:
    price = km * 0.50
print (f"Total a pagar: R${price:.2f}")
