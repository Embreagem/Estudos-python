# Faça um programa que laia um ano qualquer a mostre se ala é BISSEXTO

ano = int(input("Qual o ano? "))

d4 = ano % 4 == 0
d100 = ano % 100 == 0
d400 = ano % 400 == 0

if d4 and not d100 or d400:
    print(f"{ano} é bissexto")
else:
    print(f"{ano} não é bissexto")