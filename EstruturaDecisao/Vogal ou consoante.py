letras = ['a', 'e', 'i', 'o', 'u']
letra = input('Digite uma letra: ')

if letra in letras:
    print(f'A letra "{letra}" é vogal')
else:
    print(f'A letra "{letra}" é consoante')
