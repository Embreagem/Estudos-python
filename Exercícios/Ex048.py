"""Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500"""

#Inicializa a variável 'soma' com o valor0
soma = 0

#Cria um loop que vai percorrer os números de 3 até 499, de 3 em 3
for c in range(3, 500, 3):
    # Verifica se o número 'c' é ímpar
    if c % 2 != 0:
        # Se o número for ímpar, soma ele à variável 'soma'
        soma += c

# Quando o loop terminar, imprime o valor da variável 'soma'
# Esse valor será a soma de todos os números ímpares múltiplos de 3 entre 3 e 499
print(soma)       