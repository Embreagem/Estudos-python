# Cria um programa que leia o nome da uma cidade e diga se ela começa ou não com a palavra SANTO

nome = input("Digite um nome de uma cidade: ").strip()

nome = nome.upper()
nome = nome.split()

if nome[0].find("SANTO") != -1:
    print ("Tem a palavra (Santo)")
else: 
    print ("Nao tem a palavra (Santo)")
    