import os

os.system("cls")

# EXEMPLO 2 - TUPLAS

tupla_vazia = ()
tupla_elemento1 = (1,)
tupla_varios = (10, "Python", 2.5)
tupla_numeros = (1, 5, 9, 12, 20)

print(type(tupla_elemento1))
print(tupla_varios[1])

# Tuplas são imutáveis, porem podem ser concatenadas e multiplicadas com + e *

tupla_elemento1 = tupla_elemento1 + tupla_varios
print(tupla_elemento1)

# Checando se valor existe em tupla (Também serve pra lista)

print(10 in tupla_varios)

# Desconstrução de Tupla

a, b, c = tupla_varios
print (a, b, c)

# Tupla ordenada

print(sorted(tupla_numeros))

# Inserindo dados em uma tupla

nome = input("Nome: ")
numero = int(input("Numero: "))
valor = float(input("Quantidade de dinheiro: "))

tupla_insert = (nome, numero, valor)

print(tupla_insert)
