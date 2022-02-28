"""Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, 
se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo. """

def f(num):
    if num > 0:
        print(f'The number is positive: {num}')
    elif num < 0:
        print(f'The number is negative: {num}')

num = float(input('Qual é o número que desejas digitar? '))
print(f(num))