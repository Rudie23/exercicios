
numero = int(input('Digite um número: '))
fatorial = 1

for i in range(1, numero + 1):
    fatorial = fatorial * i
    print(fatorial)
print('\n')
print('Fatorial de ' + str(numero) + ' é ' + str(fatorial))