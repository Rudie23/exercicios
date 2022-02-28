class Pessoa():
    def __init__(self, nome, nascimento):
        self.nascimento = nascimento
        self.nome = nome
    def idade(self, hoje):
        hd, hm, ha = hoje
        nd, nm, na = self.nascimento
        x = ha - na
        return x

if __name__ == '__main__':
    hoje = 28, 2, 2022
    self.nascimento = 23, 9, 1995
    print(Pessoa.idade(hoje, self.nascimento))


