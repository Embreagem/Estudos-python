from colorama import Fore, Style

valor = float(input("Qual o valor da casa? R$ "))
salario = float(input("Qual o seu salário? R$ "))
anos = int(input("Em quantos anos deseja pagar? "))

meses = anos * 12
prest = valor / meses
limite = salario * 0.30

print(f"O valor das prestações é de: R${prest:.2f} reais")

if prest <= limite:
    print(Fore.GREEN + "Empréstimo aprovado!" + Style.RESET_ALL)
else:
    print(Fore.RED + "Empréstimo negado, pois a prestação não pode ultrapassar 30% do seu salário." + Style.RESET_ALL)