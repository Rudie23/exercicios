class Calculadora:

    def __init__(self, a, b):
        self.b = b
        self.a = a

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b

if __name__ == '__main__':
    c = Calculadora(1,2)
    c.a = 10
    c.b = 5
    print(c.soma())
    print(c.subtracao())
    print(c.multiplicacao())
    print(c.divisao())
