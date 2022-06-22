def ola_mundo():
    return 'Olá, Mundo!'


print(ola_mundo())


# Parâmetros de Função

def hello(name, last_name):
    print()
    return f'   Hello, {name} {last_name}!'


print(hello(name=input(f"What's your first name? "), last_name=input(f"What's your last name ")))
