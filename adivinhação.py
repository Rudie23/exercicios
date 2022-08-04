total_de_tentativas = 3
rodada = 1

numero_secreto = 50

while total_de_tentativas > 0:
    print(f'Tentativa {rodada} de {total_de_tentativas}')
    chute = int(input('Digite o seu número: '))
    print('Você digitou: ', chute)
    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if acertou:
        print('Você acertou!')
        break
    elif maior:
        print('Você errou! O seu chute foi maior que o número secreto')
    elif menor:
        print('Você errou! O seu chute foi menor que o número secreto')
    rodada = rodada + 1

print('Fim do jogo')
