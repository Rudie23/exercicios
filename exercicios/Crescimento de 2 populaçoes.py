""" Exercício para saber quando a população de A superará a população de B.
    Sendo que as taxas de crescimento foram fornecidas

"""
populacao_A = 80_000
populacao_B = 200_000

taxa_de_crescimento_a = 1.03
taxa_de_crescimento_b = 1.015

anos = 0

while populacao_A < populacao_B:
    # print(f'Populações no ano {anos}') para não mostrar os anos intermediários
    # print(f'População de A = {populacao_A}')
    # print(f'População de B = {populacao_B}')
    anos = anos + 1
    populacao_A = int(populacao_A * taxa_de_crescimento_a)
    populacao_B *= taxa_de_crescimento_b
    populacao_B = int(populacao_B)

print(f'Populações no ano {anos}')
print(f'População de A = {populacao_A}')
print(f'População de B = {populacao_B}')
