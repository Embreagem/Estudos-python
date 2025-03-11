
soma = 0  # Vai armazenar a soma das idades
media = 0  # Será usada para calcular a média de idade
idadeMV = 0  # Vai armazenar a idade do homem mais velho
nomeMV = ""  # Vai armazenar o nome do homem mais velho
quantF = 0  # Vai contar as mulheres com menos de 20 anos


for c in range(1, 5):  # O loop vai rodar 4 vezes (para 4 pessoas)
    print(f"--- {c}° Pessoa ---")
    nome = str(input(f"Qual o nome da {c}° pessoa?")).strip()

    while True:  # O loop vai continuar até o usuário digitar um número válido
        try:
            idade = int(input(f"Qual a idade da {c}° pessoa?"))  # Tenta converter a idade para inteiro
            break  # Se não houver erro, sai do loop
        except ValueError:  # Se ocorrer um erro  entra aqui
            print("Por favor, digite um número inteiro válido para a idade")

    print("M/F")
    while True:
        sexo = input(f"Qual o sexo da {c}° pessoa?").upper()  # Pede o sexo e converte para maiúsculo
        if sexo == "M" or sexo == "F":  # Verifica se a entrada é válida
            break  # Se for válida, sai do loop
        else:
            print("Digite uma opção válida para esse campo (M/F)")  # Mensagem de erro se a entrada for inválida

    soma += idade
    
    # Lógica para encontrar o homem mais velho
    if c == 1 and sexo == "M":  # Se for a primeira pessoa e for homem
        idadeMV = idade  # A idade dele é a mais velha até agora
        nomeMV = nome  # O nome dele é o do homem mais velho até agora

    # Se for homem e a idade dele for maior do que a idade do homem mais velho
    if sexo == "M" and idade > idadeMV:  
        idadeMV = idade  # Atualiza a idade do homem mais velho
        nomeMV = nome  # Atualiza o nome do homem mais velho

   
    if sexo == "F" and idade < 20:
        quantF += 1  # Incrementa o contador de mulheres com menos de 20 anos
        

media = soma / 4

# Exibe os resultados
print(f"A média de idade do grupo: {media}")  
print(f"Nome do homem mais velho: {nomeMV}")
print(f"Mulheres que têm menos de 20 anos: {quantF}") 