def minha_funcao(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')


minha_funcao(nome='Diego')

print()

# Também podemos passar um dicionário acrescido de dois asteriscos, já que se trata de chave e valor

dicionario = {'nome': 'Diego', 'idade': 26}
minha_funcao(**dicionario)
