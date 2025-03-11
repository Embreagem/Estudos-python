#Cria um programa que leia dois valores a mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
#seu programa deverá realizar a operação solicitada em cada caso.
import time
a = int(input("Digite um número "))
b = int(input("Digite outro número "))
opção = 0
while opção != 5:
    
    print (" "*20)
    print ("-----Menu-----")
    print (" "*20)
    opção = int(input(" [1] somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa "))
    
    if opção == 1:
        soma = a + b
        print (f"A soma de {a} e {b} é {soma}")
    
    if opção == 2:
        if a == 0 or b == 0:
            print ("Divisão por zero!")
        multip = a * b
        print (f"{a} vezes {b} é {multip}")
    
    if opção == 3:
        if a > b:
            print (f"{a} é o maior número")
        elif b > a:
            print (f"{b} é o maior número")
        elif a == b:
            print (f"Números iguais")
    
    if opção == 4:
        a = int(input("Digite um número"))
        b = int(input("Digite outro número"))
        
        
    if opção > 5:
        print ("Digite uma opção válida!")
    time.sleep(2)
print ("progama finalizado")        