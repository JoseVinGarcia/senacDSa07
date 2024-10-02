import os

os.system("cls")

# EXERCICIO 1 - FUNCOES

def calculo_par(a,b):
    if a % 2 == 0:
        re1 = "Verdadeiro"
    else:
        re1 = "Falso"
    if b % 2 == 0:
        re2 = "Verdadeiro"
    else:
        re2 = "Falso"

    return re1, re2


ev1 = int(input("Insira o primeiro numero: "))
ev2 = int(input("Insira o segundo numero: "))

resultado1, resultado2 = calculo_par(ev1, ev2)

print(f"O primeiro valor é {resultado1} e o segundo é {resultado2}")
