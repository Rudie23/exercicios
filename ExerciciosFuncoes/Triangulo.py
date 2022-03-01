def triangulo(n: 1):
    for linha in range(1, n + 1):
        for _ in range(linha):
            print(linha, end='   ')
        print('')


print('Triangulo com 1')
triangulo(1)
print('Triangulo com 2')
triangulo(2)
print('Triangulo com 3')
triangulo(3)
print('\n\n')


def triangulo(n: 1):
    for linha in range(1, n + 1):
        for coluna in range(1, linha + 1):
            print(coluna, end='   ')
        print('')


print('Triangulo com 1')
triangulo(1)
print('Triangulo com 2')
triangulo(2)
print('Triangulo com 3')
triangulo(3)
