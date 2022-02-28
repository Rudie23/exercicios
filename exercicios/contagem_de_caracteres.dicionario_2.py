def contar_caracteres(s):
    """Função que conta os caracteres

    >>> contar_caracteres('Diego')

    {'d':1, 'e':1, 'g':1, 'i':1, 'o':1}

    >>> contar_caracteres("Andrade")

    {'a':2, 'd':2, 'e':1, 'n':1, 'r':1}
    """

    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado


if __name__ == '__main__':
    print(contar_caracteres('Diego'.lower()))
    print()
    print(contar_caracteres('Andrade'.lower()))