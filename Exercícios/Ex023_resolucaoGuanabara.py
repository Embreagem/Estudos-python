
number = int(input("Digite um numero de 0 a 9999 "))
print(f"Esse numero: {number} possui:")
u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10
print(f" {u} unidade(s)")
print(f" {d} dezena(s)")
print(f" {c} centena(s)")
print(f" {m} milhar(es)")


# Explicação do código:

# 1. Entrada do número:
#    O programa pede para o usuário digitar um número de 0 a 9999 e o converte para um número inteiro com int(), armazenando na variável number.

# 2. Cálculo da unidade (u):
#    A operação number // 1 não altera o número, mas o uso de % 10 retorna o resto da divisão por 10, ou seja, o último dígito do número (unidade).
#    Exemplo: Para 1834, 1834 % 10 dá 4.

# 3. Cálculo da dezena (d):
#    number // 10 remove a unidade, deixando 183, e ao fazer 183 % 10, obtemos o resto da divisão por 10, que é 3 (a dezena).
#    Exemplo: Para 1834, 1834 // 10 = 183 e 183 % 10 = 3.

# 4. Cálculo da centena (c):
#    number // 100 remove a unidade e a dezena, deixando 18, e ao fazer 18 % 10, obtemos o resto da divisão por 10, que é 8 (a centena).
#    Exemplo: Para 1834, 1834 // 100 = 18 e 18 % 10 = 8.

# 5. Cálculo do milhar (m):
#    number // 1000 remove unidade, dezena e centena, deixando 1, e ao fazer 1 % 10, obtemos 1 (o milhar).
#    Exemplo: Para 1834, 1834 // 1000 = 1 e 1 % 10 = 1.

# Resultado final:
# O código imprime os valores de unidade, dezena, centena e milhar, dependendo do número digitado.