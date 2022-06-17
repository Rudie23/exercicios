"""Vamos corrigir a lição de casa de criação de um programa para calcular a média de uma
sequência de números arbitrários fornecida pelo usuário do sistema."""

print("Para saber a soma e a média dos números")
soma = float(input('Digite um número: '))

for n in range(2, 4):
    soma += float(input('Digite outro número: '))
    media = soma / n
    print(f'A soma dos números é {soma} e a média é {media}')
