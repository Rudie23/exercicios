""" Como fazer programa em Python que compara conteúdo e tamanho de strings """

s1 = input('Digite uma string: ')
s2 = input('Digite outra string: ')

tamanho1 = len(s1)
tamanho2 = len(s2)

print(f'"{s1}": {tamanho1} caracteres')
print(f'"{s2}": {tamanho2} caracteres')

comparacao_de_tamanho = 'diferentes'
comparacao_de_conteudo = 'diferentes'

if s1 == s2:
    comparacao_de_tamanho = 'iguais'
    comparacao_de_conteudo = 'iguais'
elif tamanho1 == tamanho2:
    comparacao_de_tamanho = 'iguais'

print(f'As duas strings são de tamanhos {comparacao_de_tamanho}.')
print(f'As duas strings possuem conteúdos {comparacao_de_conteudo}')
