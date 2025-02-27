print ("Faça um programa que laia um número de 0 a ۹۹۹۹ a mostra na tala cada um dos digitos separados.\nEx:\nDigita um número: 1834\nunidade: 4\ndezena: 3\ncentena: 8\nmilhar: 1")

number = input("Digite um numero de 0 a 9999 ")
print (f"Esse numero: {number} possui:")

if len(number) == 4:
print (f" {number[0]} unidade(s)")
print (f" {number[1]} dezena(s)")
print (f" {number[2]} centena(s)")
print (f" {number[3]} milhar(es)")

elif len(number) == 3:
print (f" {number[0]} unidade")
print (f" {number[1]} dezena")
print (f" {number[2]} centena")

elif len(number) == 2:
print (f" {number[0]} unidade")
print (f" {number[1]} dezena")

elif len(number) == 1:
print (f" {number[0]} unidade")

else:
print ("Numero invalido! Digite um numero entre 0 a 9999")

