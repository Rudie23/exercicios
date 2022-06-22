
notas = [10, 5.5, 7, 9]
tamanho = len(notas)
print(f'foram lidas {tamanho} notas.')
print(' '.join([str(nota) for nota in notas]))
print(type(notas))

for nota in notas:
    print(nota, type(nota))

soma = sum(notas)
media = soma / tamanho
print(f'A soma das notas é {soma}.')
print(f'A média é: {soma/tamanho}.')

for nota in notas:
    if nota > media:
        print(nota, end=' ')

'''Ou pode ser lido'''

print(' '.join([str(nota) for nota in notas if nota > media]))
