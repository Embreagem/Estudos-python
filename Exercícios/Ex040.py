"""Cria um programa que leia duas notas da um aluno a calcula sua média, mostrando uma mensagem no final, da acordo com a média atingida:

- Média abaixo de 5.0:
REPROVADO

- Média entre 5.0 e 6.9:
RECUPERAÇÃO

- Média 7.0 ou superior:
APROVADO"""


a = float(input("Digite a 1° nota "))
b = float(input("Digite a 2° nota "))

media = (a+b)/2

if media < 5:
    print ("Reprovado")
elif media >= 5 and media <= 6.9:
    print ("Recuperacao")
elif media >= 7:
    print ("Aprovado")    
    
    
    