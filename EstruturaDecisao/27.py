"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
adquiridas e escreva o valor a ser pago pelo cliente.

"""

morango_sem_desconto = 2.5
maca_sem_desconto = 1.8

morango_com_desconto = 2.2
maca_com_desconto = 1.5

preco_com_desconto = 0
preco_sem_desconto = 0
morango = 0

morango = float(input('Quantos quilos de morango você quer? '))
while morango <= 5:
    preco_sem_desconto = morango_sem_desconto * morango
    print(f'O preço de morangos é R$ {preco_sem_desconto:.2f}.')
    break
while morango > 5:
    preco_com_desconto = morango_com_desconto * morango
    print(f'O preço de morangos é R$ {preco_com_desconto:.2f}.')
    break
