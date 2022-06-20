"""Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu
argumento for positivo, e ‘N’, se seu argumento for zero ou negativo. """


def f(number):
    if number > 0:
        print(f'The number is positive: {number}')
    elif number < 0:
        print(f'The number is negative: {number}')


num = float(input('Qual é o número que desejas digitar? '))
f(num)
