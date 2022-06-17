nome = 'Ruan Diego Andrade dos Anjos'.upper()

nome_invertido_por_letras = ''.join(reversed(nome))

# print(nome.split())  separa pelos espaços

nome_invertido_por_palavras = ' '.join(reversed(nome.split()))

print(f'Nome com letras em maiúsculo: {nome}')
print(f'Nome com letras em maiúsculo invertido por letras: {nome_invertido_por_letras}')
print(f'Nome com letras em maiúsculo invertido por palavras: {nome_invertido_por_palavras}')
