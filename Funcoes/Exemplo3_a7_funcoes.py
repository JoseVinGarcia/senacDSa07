import os

os.system("cls")

# EXEMPLO 1 - FUNCOES/MÉTODOS

# Criando Funcao

def decoracao():
    print("=" * 20)


decoracao()
print("INICIANDO PROGRAMA\n")

print("Nome: ")
print("Idade: ")
print("Cidade: ")

decoracao()
print("DADOS PESSOAIS\n")

print("RG: ")
print("CPF: ")

decoracao()
print("REDES SOCIAIS\n")

print("Linkedin: ")
print("Instagram: ")

# EXEMPLO 2 - FUNCAO COM ARGUMENTOS

def saudacao(txt):
    print(f"Olá {txt}!")


nome = input("\n\nInforme seu nome: ")

saudacao(nome)

# EXEMPLO 3 - Soma

def somar(a, b):
    return a + b, (a + b)/2


n1 = int(input("\n\nInforme seu numero: "))
n2 = int(input("Informe seu numero: "))

total, medium = somar(n1, n2)

print(f"Total é: {total} e a média é {medium}.")