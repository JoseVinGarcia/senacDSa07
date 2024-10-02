import os

os.system("cls")

# ATIVIDADE 2 - TUPLAS

print("Boa tarde, tudo bem? Digite 5 números:")

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))
n4 = int(input("Número 4: "))
n5 = int(input("Número 5: "))

tupla = (n1, n2, n3, n4, n5)

print(f"\nTodos os valores: {tupla}")
print(f"Tupla ordenada: {sorted(tupla)}")
print(f"Maior número: {max(tupla)}")
print(f"Menor número: {min(tupla)}")
print(f"Valor total: {sum(tupla):.2f}") #:.2f define a quantidade de casas decimais (2 nesse caso)
