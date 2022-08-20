def change(c):
    if str.islower(c):
        return str.upper(c)
    else:
        return str.lower(c)


def swap_case(s: str):
    return ''.join(map(change, s))


nome = 'Ruan Diego'

print(swap_case(nome))
