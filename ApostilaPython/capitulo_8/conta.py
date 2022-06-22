import datetime


class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Historico:

    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f'Data de abertura da conta: {self.data_abertura}')
        print('Transações: ')
        for t in self.transacoes:
            print('-', t)


class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):
        print("Inicializando uma conta")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo = self.saldo + valor
        self.historico.transacoes.append(f'Depósito de {valor}')

    def saca(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo = self.saldo - valor
            self.historico.transacoes.append(f'Saque de {valor}')
            return True

    def extrato(self):
        print(f'O número: {self.numero} \nsaldo: {self.saldo} ')
        self.historico.transacoes.append(f'Tirou o extrato - saldo de {self.saldo}')

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if not retirou:
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(f'Transferência de {valor} para conta {destino.numero}')
            return True


c1 = Conta('123-4', 'Diego', 120.0, 1000.0)
c2 = Conta('123-4', 'Diego', 120.0, 1000.0)

if c1 == c2:
    print('contas iguais')
else:
    print('contas diferentes')

cliente = Cliente('Ruan Diego', 'Andrade', '1111111111-1')
conta = Conta('432-1', cliente, 120, 1000)

print(conta.titular.nome)

print()
print(type(conta.numero))
# <class 'str'>
print(type(conta.saldo))
# <class 'float'>
print(type(conta.titular))
# <class '__main__.Cliente'>

# Testando transferencias entre contas diferentes
cliente1 = Cliente('José', 'Oliveira', '1111111111-11')
cliente2 = Cliente('Diego', 'Andrade', '2222222222-22')
conta1 = Conta('123-4', cliente1, 1000)
conta2 = Conta('234-5', cliente2, 1000)

# deposita na conta 1
conta1.deposita(100)
# saca da conta 1
conta1.saca(50)
# Transferência da conta 1 para conta 2
conta1.transfere_para(conta2, 200)
conta1.extrato()

print()
# Histórico da conta 1
conta1.historico.imprime()

print()
# Histórico da conta 2
conta2.historico.imprime()
