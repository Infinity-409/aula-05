"""Aquecimento FINAL:
Solicite ao usuário que informe
notas enquanto desejar e, ao ﬁnal,
informe a média das notas digitadas."""

contador = 1
soma = 0

while True:
    nota = int(input(f"Digite a {contador}ª nota: "))
    soma = soma + nota
    resposta = int(input("Deseja continuar?\n[1] Sim\n[2] Nao\n"))
    if resposta == 2:
        break
    else:
        contador = contador + 1

media = soma/contador
print(media)