"""" Faça um programa que leia 5 números e informe o maior número"""

print("Para saber qual é o maior número")
maximo = int(input('Digite um número: '))

for _ in range(1): # _ ao invés de i para ver apenas os valores que voce digitar
    maximo = max(maximo, int(input('Digite outro número: ')))
    print(f'Numero maximo encontrado até agora é: {maximo}')
