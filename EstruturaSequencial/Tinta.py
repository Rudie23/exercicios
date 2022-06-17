"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os
valores para cima, isto é, considere latas cheias."""

import math


print('                                 Programa para informar ao cliente o quanto ele pagará para pintar.')
print('Há duas tintas disponíveis: uma é vendida, por R$ 80,00, em uma lata de 18 litros e a outra é vendida, '
      'por R$ 25,00, em uma galão de 3,6 litros.')
print('')

lata_litros = 18
galao_litros = 3.6

valor_lata = 80
valor_galao = 25

area_pintar = int(input('Informe a área que será pintada: '))
area_total_pintar = area_pintar * 1.1
print(f'A área com folga a ser pintada será de: {area_total_pintar:.2f} m².')

cobertura_por_litro = 6
cobertura_total = area_total_pintar / cobertura_por_litro
print(f'A cobertura da tinta é de 1 litro por {cobertura_por_litro} metros.')
print(f'A cobertura total da tinta é de {cobertura_total:.2f} de m² por litro.')
print('')


# Compra somente usando latas

numero_de_latas = math.ceil(cobertura_total / lata_litros)
print(f'O número de latas necessário é de: {numero_de_latas}.')

valor_so_latas = numero_de_latas * valor_lata
print(f'O valor a pagar comprando somente latas é de R$ {valor_so_latas:.2f}.')
print('')


# Compra somente usando galões

numero_de_galoes = math.ceil(cobertura_total / galao_litros)
print(f'O número de galões necessário é de: {numero_de_galoes}.')

valor_so_galoes = numero_de_galoes * valor_galao
print(f'O valor a pagar comprando somente galões é de R$ {valor_so_galoes:.2f}.')
print('')


# Compra otimizada

numero_de_latas_otimizado = math.floor(cobertura_total / lata_litros)
print(f'O número de latas otimizado necessário é de: {numero_de_latas_otimizado}.')
valor_otimizado_latas = numero_de_latas_otimizado * valor_lata
print('')

litros_restantes = cobertura_total % lata_litros
print(f'Litros restantes: {litros_restantes}')
print('')

numero_de_galoes_otimizado = math.ceil(litros_restantes / galao_litros)
print(f'O número de galões otimizado é de: {numero_de_galoes_otimizado}.')
valor_otimizado_galoes = numero_de_galoes_otimizado * valor_galao
print('')

print(f'O valor otimizado para a compra de tintas é de R$ {(valor_otimizado_latas + valor_otimizado_galoes):.2f}.')
