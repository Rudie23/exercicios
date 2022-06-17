"""Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes."""

letra = input('Digite a letra: ').lower()

if letra in ('a', 'e', 'i', 'o', 'u'):
    print(letra, 'é uma vogal')
else:
    print(letra, 'é uma consoante')
