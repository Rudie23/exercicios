number = 55
centenas_str = dezenas_str = unidades_str = ''
centenas_int, number = divmod(number, 100)  # resultado da divisão inteira divmod(numerador, divisor). na parte esquerda
# centenas_int é o parametro que tem o resultado da divisao inteira
# number é o segundo parametro/variavel que irá recebr o resto

partes_numericas = 0

if centenas_int == 1:
    partes_numericas += 1
    centenas_str = '1 centena'
elif centenas_int > 1:
    centenas_str = f' {centenas_int} centenas'
    partes_numericas += 1

dezenas_int, number = divmod(number, 10)

if dezenas_int == 1:
    partes_numericas += 1
    dezenas_str = '1 dezena'

elif dezenas_int > 1:
    partes_numericas += 1
    dezenas_str = f' {dezenas_int} dezenas'

if number == 1:
    partes_numericas += 1
    unidades_str = '1 unidade'
elif number > 1:
    partes_numericas += 1
    unidades_str = f' {number} unidades'

if partes_numericas == 0:
    print('Número 0 não possui centenas, dezenas ou unidades')

elif partes_numericas == 1:
    print(centenas_str + dezenas_str + unidades_str)

elif partes_numericas == 3:
    print(f'{centenas_str}, {dezenas_str}, {unidades_str}')

elif partes_numericas == 2:
    if centenas_str != '':
        segunda_parte = dezenas_str + unidades_str
        print(f'{centenas_str} e {segunda_parte}')
    else:
        print(f'{dezenas_str} e {unidades_str}')
