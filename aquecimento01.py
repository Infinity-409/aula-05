"""Peça para o usuário digitar dois nomes
e imprima o maior deles utilizando F-STRING.
Se forem do mesmo tamanho,
mostre uma mensagem para tal possibilidade."""
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")

if len(nome1) > len(nome2):
    print(f"{nome1} tem mais letras que {nome2}")
elif len(nome1) < len(nome2):
    print(f"{nome2} tem mais letras que {nome1}")
else:
    print("Os dois nomes tem o mesmo tamanho!")