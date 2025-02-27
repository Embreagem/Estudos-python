print ("Cria um programa que leia o nome completo de uma pessoa a mostra:\n› O nome com todas as letras maiúsculas\n› O nome com todas minúsculas.\n› Quantas letras ao todo (sem considerar espaços).\n› Quantas letras tem o primeiro nome.")

# Solicita ao usuário que digite seu nome completo e remove espaços extras no início e no fim
nome = input("Digite seu nome completo: ").strip()

# Exibe o nome todo em letras maiúsculas
print(f"Em maiúsculas: {nome.upper()}")

# Exibe o nome todo em letras minúsculas
print(f"Em minúsculas: {nome.lower()}")

# Conta quantas letras há no nome, desconsiderando os espaços, e exibe o resultado
print(f"Ao todo, tem {len(nome.replace(' ', ''))} letras")  # Substitui os espaços por nada antes de contar

# Divide o nome em partes (separando pelos espaços) e armazena cada parte em uma lista
nome = nome.split()

# Exibe o primeiro nome e a quantidade de letras que ele possui
print(f"O primeiro nome ({nome[0]}) tem {len(nome[0])} letras")