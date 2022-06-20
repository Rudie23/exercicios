file = open('palavras.txt', 'r')
words = []

for row in file:
    row = row.strip()
    words.append(row)

file.close()
