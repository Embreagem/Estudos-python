#Faça um programa que leia o peso de
#cinco pessoas. No final, mostre qual
#foi o maior e o menor dos peso lido.

lista =[]
for c in range(1,6):
    peso = float(input(f"Quanto a {c}° pessoa pesa? "))
    lista.append(peso)

lista.sort()
print (f"O menor peso registrado foi {lista[0]}kg")
print (f"O maior peso registrado foi {lista[-1]}kg")



