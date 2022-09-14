contador = 1
maior = 0
menor = 0

while contador <= 3:
    numero = int(input(f"Digite o {contador} numero: "))
    if contador == 1:
        maior = numero
        menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    contador += 1

print(menor)
print(maior)