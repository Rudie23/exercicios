"""
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
"""

string = 'FULANO'
lenght = len(string)

for row in range(lenght):
    for col in range(row + 1):
        print(string[col], end='')
    print()
