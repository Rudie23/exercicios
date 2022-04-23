def ola_mundo():
    return 'Olá, Mundo!'


print(ola_mundo())


# Parâmetros de Função

def ola(nome):
    return f'Olá, {nome}.'


print(ola(nome=input('Qual o seu nome? ')))


def hello(name, last_name):
    return f' Hello, {name} {last_name}!'


print(hello(name=input(f"What's your first name? "), last_name=input(f"What's your last name ")))
