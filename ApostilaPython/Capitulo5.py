lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 12, 3, 3, -52]
# declarando as nossas variáveis
maiorValor = lista[0]
menorValor = lista[0]
listaPares = []
listaImpares = []
ocorrenciasItem1 = 0
mediaElementos = 0
somaNegativos = 0
# iniciando o nosso loop:
for i in range(0, len(lista)):
    # Maior valor
    if maiorValor < lista[i]:
        maiorValor = lista[i]
    # Menor valor
    if menorValor > lista[i]:
        menorValor = lista[i]
    # Números pares
    if lista[i] % 2 == 0:
        listaPares.append(lista[i])
    # Números ímpares
    if lista[i] % 2 != 0:
        listaImpares.append(lista[i])
    # Numero de ocorrências
    if lista[i] == lista[0]:
        ocorrenciasItem1 = ocorrenciasItem1 + 1
    # Soma dos números negativos
    if lista[i] < 0:
        somaNegativos = somaNegativos + lista[i]

# Media do somatório dos elementos
mediaElementos = + mediaElementos + lista[i]
mediaElementos = mediaElementos / len(lista)
print("Maior valor: " + str(maiorValor))
print("Menor valor: " + str(menorValor))
print("Lista de elementos pares: " + str(listaPares))
print("Lista de elementos ímpares: " + str(listaImpares))
print("Número de ocorrências do primeiro item: " + str(ocorrenciasItem1))
print("Média dos elementos: " + str(mediaElementos))
print("Somatório dos valores negativos:" + str(somaNegativos))
