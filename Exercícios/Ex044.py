"""Elabora um programa que calcule o valor a ser pago por um produto. considerando o seu preço normal a condição de pagamento:

- a vista dinheiro/cheque: 10% da desconto
- à vista no cartão: 5% de desconto
em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros"""

price = float(input("Qual o preço do produto? R$ "))
print ("-"*20)
print ("Formas de pagamento")
print (" 1 - a vista dinheiro/cheque: 10% da desconto \n 2 - à vista no cartão: 5% de desconto \n 3 - em até 2x no cartão: preço normal \n 4 - Credito 3x ou mais no cartão: 20% de juros")
print ("-"*20)
metpay = int(input("Como deseja pagar o produto? "))

if metpay == 1:
    Valor_final = price - (price * 0.10)
elif metpay == 2:
    Valor_final = price - (price * 0.05)
elif metpay == 3:
    Valor_final = price
    parc = price / 2
elif metpay == 4:
    prests = int(input("Quantas vezes?"))
    Valor_final = price + (price * 0.20)
    parc = Valor_final / prests     
print (f"O novo valor ficou em R$ {Valor_final:.2f}")
if metpay == 3 or metpay == 4:
      print (f" Valor de cada parcela: R$ {parc:.2f} reais")

    
    
    