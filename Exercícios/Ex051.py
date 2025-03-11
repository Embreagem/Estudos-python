"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,mostre os 10 primeiros termos dessa progressão."""

primeiro_termo = int(input("Digite o primeiro termo da progressão "))
pt = primeiro_termo
razao = int(input("Digite a razao "))

for c in range(pt, pt +(razao*10) ,razao):
    print (c)

