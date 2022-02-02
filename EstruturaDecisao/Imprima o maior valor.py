"""Faça um Programa que peça dois números e imprima o maior deles."""

number_1 = float(input(f'Escreva um número: '))
number_2 = float(input(f'Escreva outro número: '))


if number_1 > number_2:
    print(f'{number_1} é maior')
elif number_1 < number_2:
    print(f'{number_2} é maior')
elif number_1 == number_2:
    print('Os dois são iguais')
