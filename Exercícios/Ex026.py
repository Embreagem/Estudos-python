#Faça um programa que leia uma frase palo teclado a mostre: 
#► Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#› Em que posição ela aparece a última vez

frase = input ("Digite uma frase: ").strip().upper()
position_left = frase.find("A")
position_right = frase.rfind("A")
xA = frase.count("A")

if frase.count("A") != 0:
    print (f"Quantidade de letras (A): {xA}")
    print (f"Posiçao em que aparece pela primeira vez {position_left}" )
    print (f"Posiçao em que aparece pela ultima vez {position_right}" )
else:
    print("Nao existe nenhuma letra A nessa frase")