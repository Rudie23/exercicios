letras = ['a', 'e', 'i', 'o', 'u']
letra = input('Digite uma letra: ')

for letra in letras:
    if letra in letras:
        print(f'É vogal')
