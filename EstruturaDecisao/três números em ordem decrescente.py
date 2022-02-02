
numero_1 = 30
numero_2 = 50
numero_3 = 20

if numero_1 > numero_3 and numero_2:
    if numero_2 > numero_3:
        print(f'{numero_1} < {numero_2} < {numero_3}')
    elif numero_3 > numero_2:
        print(f'{numero_1} < {numero_3} < {numero_2}')
elif numero_2 > numero_1 and numero_3:
    if numero_3 > numero_1:
        print(f'{numero_2} < {numero_3} < {numero_1}')
    elif numero_1 > numero_3: # esta linha não está executando
        print(f'{numero_2} < {numero_1} < {numero_3}')
elif numero_3 > numero_2 and numero_1:
    if numero_1 > numero_2:
        print(f'{numero_3} < {numero_1} < {numero_2}')
    elif numero_2 > numero_1:
        print(f'{numero_3} < {numero_2} < {numero_1}')
