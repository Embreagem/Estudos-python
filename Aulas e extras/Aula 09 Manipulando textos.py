# ================================
# MANIPULAÇÃO DE STRINGS E LISTAS
# ================================

# ---- TRABALHANDO COM STRINGS ----

# Criando uma string
texto = "Olá, mundo!"

# Contando quantos caracteres existem na string (inclui espaços e pontuação)
print(len(texto))  # Saída: 11

# Contando quantas vezes um determinado caractere aparece na string
frase = "banana"
print(frase.count("a"))  # Conta quantos 'a' existem na palavra "banana" (Saída: 3)

# Convertendo texto para diferentes formatos
mensagem = "Python é incrível!"
print(mensagem.upper())   # Converte toda a string para MAIÚSCULAS
print(mensagem.lower())   # Converte toda a string para minúsculas
print(mensagem.capitalize())  # Apenas a primeira letra da string fica maiúscula
print(mensagem.title())  # A primeira letra de cada palavra fica maiúscula

# Removendo espaços desnecessários no início e no final de uma string
espacado = "   Python   "
print(espacado.strip())  # Remove os espaços externos (Saída: "Python")

# Substituindo parte do texto por outro conteúdo
nova_frase = "Eu adoro programar!"
print(nova_frase.replace("adoro", "gosto de"))  # Substitui "adoro" por "gosto de"

# Separando uma string em uma lista de palavras com base em um separador
frutas = "maçã,banana,uva"
lista_frutas = frutas.split(",")  # Divide a string onde encontrar vírgulas
print(lista_frutas)  # Saída: ['maçã', 'banana', 'uva']

# Juntando os elementos de uma lista em uma única string
nova_string = " - ".join(lista_frutas)  # Insere " - " entre cada item da lista
print(nova_string)  # Saída: "maçã - banana - uva"

# ---- TRABALHANDO COM LISTAS ----

# Criando uma lista de números
numeros = [4, 2, 8, 1]

# Adicionando um novo número ao final da lista
numeros.append(10)  
print(numeros)  # Saída: [4, 2, 8, 1, 10]

# Contando quantas vezes um valor aparece na lista
print(numeros.count(2))  # Conta quantas vezes o número 2 aparece na lista (Saída: 1)

# Removendo um elemento específico da lista pelo seu valor
numeros.remove(8)  
print(numeros)  # Saída: [4, 2, 1, 10]

# Removendo o último elemento da lista e retornando seu valor
ultimo = numeros.pop()
print(ultimo)  # Saída: 10 (último número removido da lista)
print(numeros)  # Lista atualizada após a remoção: [4, 2, 1]

# Ordenando a lista em ordem crescente
numeros.sort()
print(numeros)  # Saída: [1, 2, 4]

# Invertendo a ordem dos elementos da lista
numeros.reverse()
print(numeros)  # Saída: [4, 2, 1]