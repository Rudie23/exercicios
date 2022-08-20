lista = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]


def islands(matrix):
    # 1 -> black
    # 2 -> white
    # Write your code here.
    for i, row in enumerate(matrix):
        print(f'index {i}', row)

    return None


islands(lista)
