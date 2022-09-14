"""Aquecimento 02:
Solicite ao usuário um número inteiro
e imprima na tela:
i) O quadrado do número caso seja par
ii) O cubo caso o número seja ímpar"""

numero = int(input("Informe um numero: "))

if (numero % 2 == 0):
    print(f"{numero} e par logo o resultado e {numero**2}")
else:
    print(f"{numero} e impar logo o resultado e {numero**3}")
