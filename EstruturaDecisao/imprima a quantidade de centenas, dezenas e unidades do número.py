
numero = 326
centenas_str = dezenas_str = unidades_str = ''

centenas_int = numero // 100

if centenas_int == 1:
    centenas_str = '1 centena'
elif centenas_int > 1:
    centenas_str = f'{centenas_int} centenas'

print(centenas_str, dezenas_str, unidades_str)

numero = 326
centenas_str = dezenas_str = unidades_str = ''

centenas_int, numero = divmod(numero, 100)

if centenas_int == 1:
    centenas_str = '1 centena'
elif centenas_int > 1:
    centenas_str = f'{centenas_int} centenas'

dezenas_int, numero = divmod(numero, 10)

if dezenas_int == 1:
    dezenas_str = '1 dezena'
elif dezenas_int > 1:
    dezenas_str = f'{dezenas_int} dezenas'

if numero == 1:
    unidades_str = '1 unidade'
elif numero > 1:
    unidades_str = f'{numero} unidades'

print(centenas_str, dezenas_str, unidades_str)