maior = 0
for c in range(0, 2):
    num = int(input('Digite um número: '))
    if c == 0:
        maior = num
    else:
        if num > maior:
            maior = num
print(f'O maior número digitado foi {maior}.')