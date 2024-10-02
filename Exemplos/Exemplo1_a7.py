import os

os.system("cls")

# EXEMPLO 1
# Pegando dados e criando listas vazias
dsemana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
psemana = ["Nublado", "Chuvoso", "Tempestade", "Ensolarado", "Ensolarado"]

densolarado = []
dnublado = []

# Percorre lista
# for i in range(len(psemana)):
#     if psemana[i] == "Ensolarado":
#         densolarado.append(dsemana[i])
#     else:
#         dnublado.append(dsemana[i])

# VERSÃO COM ENUMERATE
for i, v in enumerate(psemana):
    # print(i, v)
    if psemana[i] == "Ensolarado":
        densolarado.append(dsemana[i])
    else:
        dnublado.append(dsemana[i])

# Exibe dias ensolarados
print(f"Dias ensolarados: {densolarado}")

# Exibe dias nublados
print(f"Dias nublados: {dnublado}")
