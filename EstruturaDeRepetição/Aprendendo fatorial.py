n = int(input('Informe um número para obter o seu fatorial: '))
c = n
f = 1

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print(f'{f}')
