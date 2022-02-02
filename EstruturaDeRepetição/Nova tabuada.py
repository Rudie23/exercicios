"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
"""

tabuada = int(input('Informe o número da tabuada que deseja: '))
i = 0
while i < 10:
    i += 1
    print(tabuada, 'x', i, '=', tabuada*i)

