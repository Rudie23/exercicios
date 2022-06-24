def teste(arg, *args):
    print(f'Primeiro argumento normal: {arg}')
    for arg in args:
        print(f'Outro argumento: {arg}')


teste('python', 'é', 'muito', 'legal')

print()

lista = ['é', 'muito', 'legal']
teste('Python', *lista)

print()

tupla = ('é', 'muito', 'legal')
teste('Python', *tupla)
