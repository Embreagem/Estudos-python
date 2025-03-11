"""Refaça o DESAFIO 035 dos triângulos. acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
-Isóscales: dois lados iguais
- Escaleno: todos os lados diferentes"""

a = float(input("Comprimento lado A "))
b = float(input("Comprimento lado B "))
c = float(input("Comprimento lado C "))

reta = (a+b > c) and (b+c > a) and (c+a > b)

if reta == True:
    print ("Esse conjunto forma um triangulo"))
    if a == b and  b == c:
        print ("Esse conjunto forma um triangulo equilátero!")
    elif a == b or a == c or b == c:
    print ("Esse conjunto forma um triangulo isóscales")
else:
    print ("Esse conjunto forma um triangulo escaleno")

