"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os
números IMPARES no vetor impar. Imprima os três vetores. """
numbers = list(range(1, 21))
odd = []
even = []
for number in numbers:
    if number % 2 != 0:
        odd.append(number)
    else:
        even.append(number)

print('São pares:', even)
print('São ímpares:', odd)
