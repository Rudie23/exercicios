"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
preço total. """

import math

area_a_ser_pintada = float(input(f'Informe a área a ser pintada: '))

litros_por_metro = 3
latas_de_18 = 80

cobertura_da_tinta = area_a_ser_pintada / litros_por_metro
print(f'quantidade de litros a serem usados {cobertura_da_tinta:.2f} litros')
quantidade_de_latas_de_18 = cobertura_da_tinta / 18
   # if quantidade_de_latas_de_18 == float:
  #     quantidade_de_latas_de_18 = int
      # quantidade_de_latas_de_18 += 1
preco = latas_de_18 * math.ceil(quantidade_de_latas_de_18)

print('\n')
print(f'A quantidade de latas a serem usadas será de {math.ceil(quantidade_de_latas_de_18)}')
print(f'O valor total a ser pago será de R$ {preco}')