
nw = input("Digite algo")

print ("O tipo é:", type(nw))
#type etorna o tipo da variável (<class 'str'> para strings).


print ("é numerico?", nw.isnumeric())
# .isnumeric(): Verifica se a string contém apenas números (True ou False).


print ("Está em maiusculo?", nw.isupper())
# .isupper(): Verifica se todos os caracteres são maiúsculos.


print ("está em minusculo?", nw.islower())
# .islower(): Verifica se todos os caracteres são minúsculos


print ("Alpha?", nw.isalpha())
# .isalpha(): Verifica se a string contém apenas letras (True ou False).


print ("Numero ou letra?", nw.isalnum()) 
# .isalnum(): Verifica se a string contém apenas letras e/ou números (True ou False).


print ("apenas espaços?", nw.isspace())
# .isspace(): Verifica se a string contém apenas espaços em branco (True ou False)


print ("Capitalizado?", nw.istitle())
# .istitle(): Verifica se a string está capitalizada (primeira letra de cada palavra maiúscula).


print ("Decimal?", nw.isdecimal())
# .isdecimal(): Verifica se a string contém apenas números decimais (True ou False).


print ("pode ser identificador?", nw.isidentifier())
# .isidentifier(): Verifica se a string pode ser usada como um nome de variável válido.


print("pode ser impresso?", nw.isprintable())
# .isprintable(): Verifica se todos os caracteres podem ser impressos (sem caracteres de controle como \n ou \t).