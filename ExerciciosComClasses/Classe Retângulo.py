"""
Classe Retangulo: Crie uma classe que modele um retangulo:

    a) Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
    b) Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
    c) Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois,
    deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

"""

class Retangulo:

    def __init__(self, largura, comprimento):
        self.largura = largura
        self.comprimento  = comprimento

    def area(self):
        return f'A área é de {self.largura * self.comprimento} metros'


largura = float(input('Qual a largura? '))
comprimento = float(input('Qual o comprimento? '))

retangulo = Retangulo(largura, comprimento)
print(retangulo.area())

