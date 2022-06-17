while True:
    try:
        numero = int(input('Informe um numero: '))
    except ValueError:
        print('Deve ser informado um valor inteiro')
    else:
        if 0 <= numero <= 10:
            print(f'O numero informado foi de {numero}')
            break
        else:
            print('O número informado deve estar entre 1 e 10')
