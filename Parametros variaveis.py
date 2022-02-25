def soma(*args):
    aux = 0
    for valor in args:
        aux = aux + valor  # aux += valor
    return aux


print(soma(2, 5))


def f(**kwargs):
    print(kwargs)
    print(type(kwargs))


print(f(nome='Diego'))

nome = ''
sobrenome = ''
def f(*args, **kwargs):
    kwargs = {'nome':'', 'sobrenome': ''}
    print(**kwargs)



print(f(1, 2, 'nome' == 'Diego', 'sobrenome' == 'Andrade'))


