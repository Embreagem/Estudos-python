# Especificadores de formatação

nome = input("Digite algo: ")
print(f"|{nome:<20}|")
   #Alinha à esquerda em 20 espaços
print(f"|{nome:>20}|")
   # Alinha à direita em 20 espaços 
print(f"|{nome:^20}|") 
   # Centraliza em 20 espaços
print(f"|{nome:<20}|") 
   # Preenche com '' e alinha à esquerda
print(f"|{nome:>20}|")
   # Preenche com '' e alinha à direita
print(f"|{nome:-^20}|") 
   # Preenche com '-' e centraliza


#2. Formatação de Números
num = int(input("type the number"))
print(f"Decimal: {num:d}")
   # Número decimal padrão
print(f"Binário: {num:b}")  
   # Representação binária 
print(f"Octal: {num:o}") 
   # Representação octal 
print(f"Hexadecimal minúsculo: {num:x}") 
   # Hex minúsculo
print(f"Hexadecimal maiúsculo: {num:X}")
   # Hex maiúsculo
print(f"Hexadecimal com prefixo: {num:#x}")     # Hex com '0x'
 

#3. Números Decimais e Casas Decimais
pi = float(input("type the number float"))
print(f"Duas casas decimais: {pi:.2f}") 
   # Apenas duas casas 
print(f"Notação científica minúscula: {pi:.2e}")  # Notação científica
print(f"Notação científica maiúscula: {pi:.2E}")  # Notação científica maiúscula  
print(f"Formato inteligente: {pi:.2g}") 
   # Escolhe entre float e exponencial


#4. Formatação de Moeda e Números Grandes

valor = (1000000)

print(f"Separador de milhares: {valor:,}")
   #Usa vírgula como separador 
print(f"Separador com : {valor:}")
   # Usa _ como separador
print(f"Moeda formatada: R${valor:,.2f}")
   # Formata como dinheiro


#5. Exibindo Sinais em Números
numpositivo = (42) 
numnegativo = (-42) 
print (f"Sempre com sinal positivo: {numpositivo:+d}")  
# Mostra o + 
print(f"Negativos com - apenas: {numnegativo:-d}") 
 # Apenas - quando necessário 
print(f"Espaço antes de positivos: {numpositivo: d}") 
 # Adiciona espaço antes de +


#6. Formatação de Percentual
taxa = (0.075)
print(f"Taxa percentual: {taxa:.2%}")
  # Converte fração para %


#7. Combinação de Formatações
nome = ("Ana")
idade = (30)
saldo = (56789.456)

print(f"Nome: {nome:<10} | Idade: {idade:>3} anos | Saldo: R${saldo:,.2f}")

