"""Cria um programa qua leia uma frase qualquer e diga se ela é um palindromo. desconsiderando os espaços."""


name = str(input("Qual o seu nome?")).strip().upper()
reverso = (name[::-1])
if reverso == name:
    print (f"{reverso} é palindromo")
else:
    print (f"{reverso} não é palindromo de {name}")

    