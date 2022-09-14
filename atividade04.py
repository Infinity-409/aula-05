"""Atividade 04:
Crie um programa que peça dez números
inteiros e positivos.
 Ao ﬁnalizar, informe separadamente
 o valor da soma dos números pares e
 dos números ímpares."""

somaPares = 0
somaImpares = 0

for contador in range(10):
    numero = int(input(f"Digite o {contador+1}º numero: "))
    if numero % 2 == 0:
        somaPares = somaPares + numero
    else:
        somaImpares = somaImpares + numero

print(f"A soma dos pares e {somaPares}.")
print(f"A soma dos impares e {somaImpares}")