""" Faça um programa que leia um vetor de 5 numeros inteiros """

lista = [1, 2, "Diego", []]

lista.append(10)
print(f'Primeira lista é {lista}')

lista = []
for _ in range(5):
    numero = float(input('Digite um número: '))
    lista.append(int(numero))

lista.sort()

print('Lista com números inteiros ordenados de forma crescente abaixo:')
print(lista)
