from datetime import date
atual = date.today().year


maior = 0
menor = 0

for c in range (1,8):
    nasc = int(input(f"Em que ano a {c}° nasceu? "))
    if atual - nasc >= 18:
        maior += 1
    else:
        menor += 1

print (f"Temos {maior} maiores de idade nessa lista")
print (f"Temos {menor} menores de idade nessa lista")



    