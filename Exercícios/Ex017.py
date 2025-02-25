from math import sqrt

print("Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.")

oposto = float(input("Qual o comprimento do cateto oposto? "))
adjacente = float(input("E o comprimento do cateto adjacente? "))

hipo = sqrt(oposto ** 2 + adjacente ** 2)

print(f"A hipotenusa é: {hipo:.2f}")