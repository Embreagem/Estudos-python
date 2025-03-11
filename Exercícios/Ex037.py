#Escreva um programa que leia um número inteiro qualquer a paça para o usuário escolher qual será a base de conversÃO:

#1 para binário
#2 para octal
#3 para hexadecimal

num = int(input("Digite um numero inteiro para a conversao "))
print (" 1 - Binario \n 2 - octal \n 3 - hexadecimal")
type = int(input("Qual o tipo de conversao? "))


bin = bin(num)
oct = oct(num)
hex = hex(num)

if type == 1:
    print (f" {num} convertido para binario é: {bin[2:]}")
elif type == 2:
        print (f" {num} convertido para octal é: {oct[2:]}")
elif type == 3:
            print (f" {num} convertido para hexagonal é: {hexagonal[2:]}")


