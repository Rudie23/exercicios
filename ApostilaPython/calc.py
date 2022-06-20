def calculadora(x, y):
    return {'soma': x + y, 'subtração': x - y}


result = calculadora(1, 2)
for key in result:
    print(f'{key}: {result[key]}')
