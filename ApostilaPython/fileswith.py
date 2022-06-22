file = open('palavras.txt', 'w')
file.write('banana\n')
file.write('uva\n')

file = open('palavras.txt', 'a')
file.write('morango\n')
file.write('manga\n')

file.close()

file = open('palavras.txt', 'r')
file.read()

# Para abrir imagens img = open('foto.jpg', 'rb')
