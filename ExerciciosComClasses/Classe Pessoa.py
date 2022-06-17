"""Classe Pessoa: Crie uma classe que modele uma pessoa:

    a) Atributos: nome, idade, peso e altura
    b) Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo
    a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.altura = altura
        self.peso = peso
        self.nome = nome
        self.idade = idade

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
        self.idade += 1


otavio = Pessoa('Otavio', 2, 12, 80)

for _ in range(20):
    otavio.envelhecer()
    print(f'Idade de {otavio.nome} é: {otavio.idade} anos. E sua altura é {otavio.altura} cm')
