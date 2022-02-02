"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar."""

print('O Super-mercado Tabajara está com uma promoção de carnes. Confira:')
print('''                   Até 5 Kg              Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
''')


file_duplo = alcatra = picanha = 0
file_duplo_kg = alcatra_kg = picanha_kg = 0

file_duplo_kg = float(input('Quantos quilos você quer de Filé Duplo: '))
if file_duplo_kg <= 5.0:
    file_duplo = 4.9
    fiLe_duplo_total = file_duplo * file_duplo_kg
elif file_duplo_kg > 5.0:
    file_duplo = 5.8
    file_duplo_total = file_duplo * file_duplo_kg

alcatra_kg = float(input('Quantos quilos você quer de Alcatra: '))
if alcatra_kg <= 5.0:
    alcatra = 5.9
    alcatra_total = alcatra * alcatra_kg
elif alcatra_kg > 5:
    alcatra = 6.8
    alcatra_total = alcatra * alcatra_kg

picanha_kg = float(input('Quantos quilos você quer de Picanha: '))
if picanha_kg <= 5.0:
    picanha = 6.9
    picanha_total = picanha * picanha_kg
elif picanha_kg > 5.0:
    picanha = 7.8
    picanha_total = picanha * picanha_kg

soma = picanha_total + alcatra_total + fiLe_duplo_total

print(f'O valor a ser pago será de: R$ {soma:.2f}')

# compra otimizada
file_duplo = alcatra = picanha = 0
file_duplo_kg = alcatra_kg = picanha_kg = 0
file_duplo_total = 0
for file_duplo_kg in range(0, 5):
    file_duplo_kg = float(input('Quantos quilos você quer de Filé Duplo: '))
    file_duplo = 4.9
    fiLe_duplo_total = file_duplo * file_duplo_kg
    for file_duplo_kg in range(5, ):
        file_duplo = 5.8
        fiLe_duplo_total = file_duplo * file_duplo_kg
print(f'O valor a ser pago será de: R$ {file_duplo_total:.2f}')


