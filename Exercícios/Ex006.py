print ("Crie um algoritimo que leia um numero, e mostre na tela: \no seu dobro / triplo / raiz quadrada.")

# Solicita um número ao usuário
num = int(input("Digite um número: "))

# Calcula o dobro, triplo e raiz quadrada
d = num * 2
t = num * 3
r = num ** 0.5  # Forma correta para calcular a raiz quadrada

# Exibe os resultados
print(f"O dobro: {d}\nO triplo: {t}\nA raiz quadrada: {r:.2f}")

#A formatação {r:.2f} significa que estamos exibindo o valor de r (raiz quadrada) com duas casas decimais.

#{r:.2f}

#r: representa a variável que será exibida.

#:.2f: significa que queremos duas casas decimais (.2) e que o número será formatado como float (f