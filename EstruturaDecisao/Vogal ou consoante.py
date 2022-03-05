letras = ['a', 'e', 'i', 'o', 'u']
letra = input('Digite uma letra: ')

if letra in letras:
    print(f'É vogal a letra "{letra}"')
else:
    print(f'É consoante a letra "{letra}"')
