#Cria um programa que leia o nome da uma pessoa a diga se ela tem "SILVA" no nome.

nome = input("Digite seu nome: ")
nome = nome.upper()
if nome.find(" SILVA ") != -1:
    print ("Tem a palavra Silva")
else:
    print ("Nao tem a palavra Silva")