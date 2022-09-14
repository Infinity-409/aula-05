"""Atividade 05:
Solicite ao usuário um limite inferior e um superior,
depois informe
quantos números pares existem no intervalo."""

limiteInferior = int(input("Limite inferior: "))
limiteSuperior = int(input("Limite superior: "))
pares = 0

for contador in range(limiteInferior, limiteSuperior+1):
    if contador % 2 == 0:
        pares = pares + 1

print(f"O intervalo possui {pares} numeros pares")
