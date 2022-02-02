
saque = int(input(f'Quanto queres sacar? '))

notas_100 = notas_50= notas_10= notas_5= notas_1 = 0

notas_100, saque = divmod(saque,100)
notas_50, saque = divmod(saque,50)
notas_10, saque = divmod(saque,10)
notas_5, notas_1 = divmod(saque,5)

if notas_100 > 0:
    print(f'{notas_100} notas de 100')

if notas_50 > 0:
    print(f'{notas_50} notas de 50')

if notas_10 > 0:
    print(f'{notas_10} notas de 10')

if notas_5 > 0:
    print(f'{notas_5} notas de 5')

if notas_1 > 0:
    print(f'{notas_1} notas de 1')

