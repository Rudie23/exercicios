x = int(input('Digite a coordenada x: '))
y = int(input('Digite a coordenada y: '))
z = int(input('Digite a coordenada z: '))
n = int(input('Digite o tamanho do cubo: '))

print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])
