coord = []

x = 0
y = 0

while True:
    x = int(input('Qual a coordenada? '))
    y = int(input('Qual a coordenada? '))

    latlong = x, y

    if x != 0 and y != 0:
        coord.append(latlong)
    else:
        break

print(coord)
print(latlong)
