letras = ['a', 'e', 'i', 'o', 'u',
          'A', 'E', 'I', 'O', 'U']
letra = input('Digite uma letra: ')

if letra in letras:
    print(f'A letra "{letra}" é vogal')
else:
    print(f'A letra "{letra}" é consoante')
