from collections import Counter


# Manipulando dicionário

colecao = [
    'cachorro', 'gato', 'cordeiro',
    'gato', 'gato', 'gato',
    'cachorro'
]

quantidades = {}

for item in colecao:
    if item not in quantidades.keys():
        quantidades[item] = 1
    else:
        quantidades[item] += 1

print(quantidades)

# Utilizando Counter

colecao = [
    'cachorro', 'gato', 'cordeiro',
    'gato', 'gato', 'gato',
    'cachorro'
]

quantidades = Counter(colecao)
print(dict(quantidades))
