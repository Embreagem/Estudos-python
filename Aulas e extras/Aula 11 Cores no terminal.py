"""
📌 Aula: Cores no Terminal (ANSI e Colorama)

No Python, podemos adicionar cores ao terminal de duas formas principais:
1️⃣ **Códigos ANSI** (nativo, sem precisar instalar nada)
2️⃣ **Biblioteca `colorama`** (mais organizada e compatível com Windows)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔹 1. Usando Códigos ANSI (Escape Sequences)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Os códigos ANSI usam `\033[` seguido de um código de cor. Exemplo:
  - `\033[31m` → Vermelho
  - `\033[32m` → Verde
  - `\033[34m` → Azul
  - `\033[m` → Reseta a cor (importante!)
"""

# Exemplo ANSI
print("\033[31mEste texto é vermelho\033[m")
print("\033[32mEste texto é verde\033[m")
print("\033[34mEste texto é azul\033[m")

"""
📌 **Códigos ANSI úteis:**
   \033[30m → Preto       |
    \033[40m → Fundo Preto
    
   \033[31m → Vermelho    |
    \033[41m → Fundo Vermelho
    
   \033[32m → Verde       |
    \033[42m → Fundo Verde
    
   \033[33m → Amarelo     |
    \033[43m → Fundo Amarelo
    
   \033[34m → Azul        |
    \033[44m → Fundo Azul
    
   \033[35m → Roxo        |
    \033[45m → Fundo Roxo
    
   \033[36m → Ciano       |
    \033[46m → Fundo Ciano
    
   \033[37m → Branco      |
    \033[47m → Fundo Branco
    
   \033[m   → Resetar cor

# Pausa para separar os testes
print("\n" + "-"*40 + "\n")

"""
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2. Usando a Biblioteca `colorama`
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#O `colorama` deixa o código mais organizado e funciona no Windows sem ajustes.

#▶ **Passo 1:** Instalar a biblioteca (se ainda não tiver)
# ```sh pip install colorama


#Importando o colorama

from colorama import Fore, Back, Style

#Exemplo Colorama

print (Fore.RED + "Este texto é vermelho" + Style.RESET_ALL)
print(Fore.GREEN + "Este texto é verde" + Style.RESET_ALL) 
print(Fore.BLUE + "Este texto é azul" + Style.RESET_ALL)

#Exemplo com fundo colorido

print (Back.YELLOW + "Texto com fundo amarelo" + Style.RESET_ALL)

#Exemplo com estilos

print(Style.BRIGHT + "Texto brilhante" + Style.RESET_ALL) 
print(Style.DIM + "Texto escurecido" + Style.RESET_ALL)

"""Comandos principais do Colorama: 
Fore. → Cor do texto

Fore.RED (Vermelho)
Fore.GREEN (Verde)
Fore.BLUE (Azul)
Fore.YELLOW,
Fore.CYAN
Fore.MAGENTA, 
e outras


Back. → Cor de fundo

Back.RED (Fundo vermelho)

Back.GREEN (Fundo verde)

Back.BLUE (Fundo azul)


Style. → Estilo do texto

Style.BRIGHT (Texto brilhante)

Style.DIM (Texto escurecido)

Style.NORMAL (Texto normal)

 Style.RESET_ALL → Reseta tudo (cor e estilo)
 

# Mensagem combinando cor do texto, fundo e estilo
mensagem = Fore.YELLOW + Back.BLUE + Style.BRIGHT + " Atenção! Isso é um alerta importante. " + Style.RESET_ALL

print(mensagem)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  Conclusão: Quando usar cada um?

Se precisar de algo rápido e simples, use códigos ANSI.

Se quiser código mais limpo e compatível com Windows, use colorama. """