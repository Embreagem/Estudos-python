"""Desenvolva um programa que leia seis números inteiros a mostra a soma apenas daqueles que forem pares. Se o valor digitado for impar. desconsidera-o."""
print("Digite seis números inteiros")

soma = 0
lista = []
for c in range(1, 7):
    num = int(input(f"Digite o {c}° número: "))
    lista.append(num)

# Somando os números pares
for num in lista:
    if num % 2 == 0:
        soma += num  # Adiciona o número par à variável soma

print("Soma dos números pares:", soma)


