frutas = {'laranja', 'banana', 'uva'}
print(frutas)
print(type(frutas))
print()

print('Frutas abacaxi e abacate em set abaixo:')
a = set('abacate')
b = set('abacaxi')

print(a)
print(b)
print()

print('Operações com o set abaixo:')
print(a - b)  # diferença
print(a | b)  # união
print(a & b)  # interseção
print(a ^ b)  # diferença simétrica
