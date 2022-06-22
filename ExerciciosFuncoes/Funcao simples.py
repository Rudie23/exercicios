def ola_mundo():
    return 'Ola Mundo'


print(ola_mundo())


# Criando parâmetros para uma função simples

def ola(nome, sobrenome):
    return f'Olá, {nome} {sobrenome}'


ola('Diego', 'Andrade')
print(ola('Diego', 'Andrade'))  # os parametros forama passados por justaposição


def ola(nome, sobrenome='Andrade', idade=26):
    return f'Olá, {nome} {sobrenome}, {idade} anos'


ola('Diego')
print(ola('Diego'))  # os parametros forama passados por justaposição


def ola(nome, sobrenome='Andrade', idade=26):
    return f'Olá, {nome} {sobrenome}, {idade} anos'


print(ola('Ruan Diego', idade=25, sobrenome='Andrade dos Anjos'))


def soma(*args):
    aux = 0
    for valor in args:
        aux += valor
    return aux


print(soma(4, 6, 50))


def f(**kwargs):
    print(kwargs)
    print(type(kwargs))


f()
f(nome='Diego')

args = (2, 4, 10)
kwargs = {'nome': 'Diego', 'sobrenome': 'Andrade'}


def f(*args, **kwargs):
    print(args)
    print(kwargs)


f()

f(1, 2, nome='Diego', sobrenome='Andrade')
f(*args, **kwargs)  # despacotei
