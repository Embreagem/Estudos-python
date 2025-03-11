# Variável para armazenar a string invertida
reverse = ""

# Aqui, eu peço o nome do usuário, removo espaços extras
# no começo e no final com strip(), transformo tudo em 
# MAIÚSCULO com upper(), divido a string em palavras 
# com split(), e depois junto tudo de novo sem espaços 
# entre as palavras com "".join().
name = str(input("Qual o seu nome?")).strip().upper().split()
name = "".join(name)

# O range vai percorrer a string ao contrário.
# - len(name) - 1 vai pegar o índice do último caractere.
# - O segundo -1 no range indica que o loop vai até o índice 0.
# - O terceiro -1 indica que a cada iteração, o índice 
# será decrementado em 1, ou seja, o 
#loop vai de trás para frente pela 
#string.
for c in range(len(name)-1, -1, -1):
    reverse += name[c]  # Adiciona o caractere atual da string invertida à variável "reverse"

# Imprime a string invertida
print(reverse)

# Compara a string original com a invertida para ver se é um palíndromo
if name == reverse:
    print(f"{name} é um palíndromo")  # Se for igual, é um palíndromo
else:
    print(f"{name} não é um palíndromo")  # Se não for igual, não é um palíndromo
    
    