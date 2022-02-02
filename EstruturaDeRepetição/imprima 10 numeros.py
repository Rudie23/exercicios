""" Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
Depois modifique o programa para que ele mostre os números um ao lado do outro.
Faça um programa que leia 5 números e informe o maior número."""

numeros = list(range(1,11))

for v in numeros:
    print(v)

i = 0
for i, v in enumerate(numeros):
    print(i, v)

print(' '.join([str(numero) for numero in numeros]))

numeros = max(numeros)

print(f'O maior número dessa lista é {numeros}!')