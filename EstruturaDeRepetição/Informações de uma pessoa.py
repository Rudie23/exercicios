'''Faça um programa que leia e valide as seguintes informações:
a) Nome: maior que 3 caracteres;
b) Idade: entre 0 e 150;
c) Salário: maior que zero;
d) Sexo: 'f' ou 'm';
e) Estado Civil: 's', 'c', 'v', 'd';
'''

while True:
    try:
        nome = input('Qual o seu nome? ')
        idade = int(input('Qual a tua idade? '))
        salario = float(input('Quanto você ganha? '))
        sexo = input('Masculino ou feminino? ')
        estado_civil = input('Qual o seu estado civil? ')
        print(nome)
        print(idade)
        print(salario)
        print(sexo)
        print(estado_civil)
    except:
        break
