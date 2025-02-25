import random

print("O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.")

nome1 = input("Digite o nome do 1° aluno: ")
nome2 = input("Digite o nome do 2° aluno: ")
nome3 = input("Digite o nome do 3° aluno: ")
nome4 = input("Digite o nome do 4° aluno: ")

alunos = [nome1, nome2, nome3, nome4]

random.shuffle(alunos)  # Embaralha a lista

print("A ordem sorteada é:")
for i, aluno in enumerate(alunos, 1):
    print(f"{i}° - {aluno}")