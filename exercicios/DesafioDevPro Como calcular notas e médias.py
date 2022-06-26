notas = []
print('Digite as notas do aluno')
while True:
    print('Para encerrar o programa, digite -1')
    entrada = float(input('Digite um número: '))
    if entrada == -1:
        break
    notas.append(entrada)

tamanho = len(notas)
print(f'Foram lidas {tamanho} notas')
print(' '.join([str(nota) for nota in notas]))  # ' '.join([str(nota) for nota in notas transformei os elementos da
# lista em string
notas.reverse()
for nota in notas:
    print(nota)

soma = sum(notas)  # sum() para somar

print(f'Soma das notas é: {soma}')
media = soma / tamanho
print(f'A média das notas é : {soma / tamanho}')

print('Notas acima da média: ')
print(' '.join([str(nota) for nota in notas if nota > media]))

print('Notas abaixo da média: ')
print(' '.join([str(nota) for nota in notas if nota < 7]))

print('Encerrado o programa')
