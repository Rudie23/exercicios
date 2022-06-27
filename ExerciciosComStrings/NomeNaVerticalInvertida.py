"""
Nome na vertical em escada invertida.
Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F

"""

s = 'FULANO'
s = s[::-1]
print(s)
while s != '':
    print(s)
    s = s[:-1]
