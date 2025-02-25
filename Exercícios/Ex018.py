from math import sin, cos, tan, radians

print("Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.")

angulo = float(input("Qual o ângulo? "))

# Converte o ângulo de graus para radianos
angulo_rad = radians(angulo)

# Calcula seno, cosseno e tangente
seno = sin(angulo_rad)
cosseno = cos(angulo_rad)
tangente = tan(angulo_rad)

# Exibe os resultados
print(f"O ângulo {angulo} possui: \nO seno: {seno:.2f} \nO cosseno: {cosseno:.2f} \nA tangente: {tangente:.2f}")