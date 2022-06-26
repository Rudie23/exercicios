"""Classe Bola: Crie uma classe que modele uma bola:

    a)Atributos: Cor, circunferência, material
    b)Métodos: trocaCor e mostraCor
"""


class CirculoPerfeitos:
    def __init__(self):
        self.cor = "Azul"
        self.circunferencia = 4
        self.material = "Papel"

    def mostra_cor(self):  # self se refere ao objeto que está executando o método
        return self.cor

    def trocar_cor(self, cor):
        self.cor = cor


circulo_primeiro = CirculoPerfeitos()
circulo_segundo = CirculoPerfeitos()
circulo_segundo.trocar_cor('Amarelo')
print(type(circulo_segundo))
print(id(circulo_primeiro), circulo_primeiro.mostra_cor())
print(id(circulo_segundo), circulo_segundo.mostra_cor())
print(circulo_primeiro.cor, circulo_segundo.cor)
