"""
Tamanho de strings.

Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
"""


def strings():
    string1 = input('Insira uma palavra qualquer: ')
    string2 = input('Insira uma outra palavra: ')

    tamanho1 = len(string1)
    tamanho2 = len(string2)

    print(f'Tamanho de "{string1}": {tamanho1} caracteres')
    print(f'Tamanho de "{string2}": {tamanho2} caracteres')

    if string1 == string2:
        print('As duas strings são de conteúdos iguais.')
        print('As duas strings são de tamanhos iguais.')
    elif tamanho1 == tamanho2:
        print('As duas strings são de conteúdos diferentes.')
        print('As duas strings são de tamanhos iguais.')


strings()
