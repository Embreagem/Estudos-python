"""Rafaça o DESAFIO 009. mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for"""

num = int(input("Digite um numero para ver sua tabuada "))

for c in range(1,11):
    tab = (num * c)
    print (f" {num} × {c} = {tab}")