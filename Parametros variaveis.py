def soma(*args):
    print(type(args))
    aux = 0
    for valor in args:
        aux = aux + valor  # aux += valor
    return aux


print(soma(2, 5))


def f(**kwargs):
    print(kwargs)
    print(type(kwargs))


print(f(nome='Diego'))
