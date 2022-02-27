def contar_caracteres(s):
    """ Função que conta os caracteres

    >>> contar_caracteres('Diego')

    d:1
    e:1
    g:1
    i:1
    o:1

    >>> contar_caracteres("Andrade")

    a:2
    d:2
    e:1
    n:1
    r:1
    """
    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f"{caracter_anterior}: {contagem}")
            caracter_anterior = caracter
            contagem = 1
    print(f'{caracter_anterior}: {contagem}')


if __name__ == '__main__':
    contar_caracteres('Diego'.lower())
    print()
    contar_caracteres('Andrade'.lower())
    print()
