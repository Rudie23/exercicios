
args = (2, 4, 10)
kwargs = {'nome': 'Diego', 'sobrenome': 'Andrade'}


def f(*args, **kwargs):
    print(args)
    print(kwargs)


f()

f(1, 2, nome='Diego', sobrenome='Andrade')
f(*args, **kwargs)  # despacotei
