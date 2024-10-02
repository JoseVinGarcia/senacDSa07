import os

os.system("cls")

# ATIVIDADE 1 - TUPLAS

print("Olá, tudo bem? Insira seus dados para cadastro: ")

nome = input("Nome: ")
cargo = input("Cargo: ")
salario = float(input("Salário: "))
idade = int(input("Idade: "))

valores = (nome, cargo, salario, idade)

print(f"Muito obrigado!\nSeus dados são os seguintes: {valores}")
