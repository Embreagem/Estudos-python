print ("Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado a a quantidade de dias pelos quais ele foi alugado. Calcula o preço a pagar, sabendo que o carro custa R$60 por dia a R$0.15 por Km rodado.")

km = float(input("Quantos km percorridos? "))
d = int(input("Quantos dias? "))

nkm = (km * 0.15) 
nd = (d * 60)
total = nkm + nd

print (f"O total a pagar é: ${total:.2f} reais")
