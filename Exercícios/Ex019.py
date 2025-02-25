import random

print ("Um professor quar sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajuda ala. lendo o nome deles a escrevendo o nome do escolhido.")

nome1 = input("Digite o nome do 1° aluno: ")
nome2 = input("Digite o nome do 2° aluno: ")
nome3 = input("Digite o nome do 3° aluno: ")
nome4 = input("Digite o nome do 4° aluno: ")

alunos = (nome1, nome2, nome3, nome4)

sorteado = random.choice(alunos)

print (f"O aluno sorteado é: {sorteado}")