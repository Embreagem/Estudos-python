#Faça um programa que leia o nome completo de uma pessoa, mostrando am seguida o primeiro a o último nome separadamente.
#Ex: Ana Maria de Souza
#primeiro = Ana
#último = Souza

nome = input("Digite seu nome: ")
print (f"Nome completo: {nome}")
nome = nome.split()
print (f"O primeiro nome é: {nome[0]}")
print (f"O ultimo nome é: {nome[-1]}")
