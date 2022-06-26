"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
identificar os usuários com maior espaço ocupado.
Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um
relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
"""

lista_de_dados = []


def transformar_em_megabytes(tamanho_em_bytes: str) -> float:
    return int(tamanho_em_bytes) / (2 ** 10) ** 2


with open('/home/diego/Documentos/usuarios', 'r') as arquivo:  # r para ler o arquivo
    for linha in arquivo:
        linha = linha.strip()  # strip para retirar as linhas
        usuario = linha[:15]
        tamanho_em_disco = transformar_em_megabytes(linha[16:])
        lista_de_dados.append((tamanho_em_disco, usuario))

print(lista_de_dados)

cabecalho = '''ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
'''

lista_de_dados.sort(reverse=True)

with open('/home/diego/Documentos/relatorio de projeto',
          'w') as arquivo:  # arquivo é uma variável a qual a função open irá interagir
    tamanho_total_consumido = sum([tamanho for tamanho, _ in lista_de_dados])
    arquivo.writelines(cabecalho)
    media = tamanho_total_consumido / len(lista_de_dados)
    for indice, dados in enumerate(lista_de_dados, start=1):  # start para começar a contar ap partir de 1
        tamanho_em_disco, usuario = dados  # despacotei
        arquivo.writelines(f''
                           f'{indice:<4} {usuario} {tamanho_em_disco:9.2f}'
                           f'{tamanho_em_disco / tamanho_total_consumido:>6.2%}\n')

    arquivo.writelines('\n\n')
    arquivo.writelines(f'Espaço total ocupado: {tamanho_total_consumido:.2f} MB \n')
    arquivo.writelines(f'Espaço médio ocupado: {media:2f} MB \n')

from random import shuffle

numeros = list(range(10))
shuffle(numeros)
print(numeros)
numeros.sort(reverse=True)
print(numeros)

print((10, 'Diego') < (8, 'Amanda'))  # R é maior que A porque vem depois dele
