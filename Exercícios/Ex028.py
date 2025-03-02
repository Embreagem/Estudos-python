import random
#gerar números aleatórios e realizar operações envolvendo aleatoriedade.
import sys
#interaja com o ambiente de execução, como obter informações sobre o sistema e manipular a execução do programa.



num = int(input("Type the number "))

range = random.randint(0,5)
# Define o intervalo
if num < 0 or num > 5:
    print ("Você digitou um numero fora do intervalo de 0 a 5")
    sys.exit()
# sys.exit interrompe a execução do codigo

if num == range:
    print (f" Você acertou!")
else:
   print (" Você errou!")
   