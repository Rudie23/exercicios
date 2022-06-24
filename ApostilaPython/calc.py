def calculadora(x, y):
    return {'soma': x + y, 'subtração': x - y}


result = calculadora(1, 2)  # a variável result é do tipo dict
print(result)
print()

for key in result:  # key
    print(type(key))
    print(type(result))
    print(type(result[key]))
    print()
    print(f'{key}: {result[key]}')

