"""
Utilizando print para gravar dados em arquivos.

A função print também pode ser utilizada para gravar dados em
arquivos. Para isso, utilizamos o parâmetro file da função print.
Além disso, precisamos de um arquivo aberto.

"""

with open('text.txt', 'w') as arquivo:
    print("Escreva isso dentro do arquivo.", file=arquivo)
    print("Escreva outra linha dentro do arquivo.", file=arquivo)
