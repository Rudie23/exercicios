"""Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e
que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento. """

pop_a = 80_000
pop_b = 200_000

tax_a = 1.03
tax_b = 1.015
anos = 0


while pop_a <= pop_b:
    anos += 1
    pop_a = int(pop_a * tax_a)
    pop_b = int(tax_b * pop_b)


print(f'Em {anos} anos, a população de A superará a população de B.')
print('população da cidade A = ' + str(pop_a) + ' habitantes')
print('popuexceptlação da cidade B = ' + str(pop_b) + ' habitantes')
