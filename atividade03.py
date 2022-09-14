"""Atividade 03:
Peça 5 números e informe
a soma de todos eles e a média"""
soma = 0

for contador in range(1, 6):
    numero = int(input(f"Informe o {contador} numero: "))
    soma = soma + numero

media = soma/contador
print(f"A soma dos numeros e: {soma}.")
print(f"A media e: {media}.")
