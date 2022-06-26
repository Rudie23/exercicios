"""
    Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

"""

respostas = []

print('Escreva sim ou não para as perguntas abaixo: ')


def telefonou():
    pergunta_telefonou = input("        Telefonou para a vítima? ").lower()
    booleano_telefonou = None
    if pergunta_telefonou == 'sim':
        booleano_telefonou = True
    else:
        booleano_telefonou = False

    respostas.append(booleano_telefonou)


def local():
    pergunta_local = input("        Esteve no local do crime? ").lower()
    booleano_local = None
    if pergunta_local == 'sim':
        booleano_local = True
    else:
        booleano_local = False

    respostas.append(booleano_local)


def mora():
    pergunta_mora = input("        Mora perto da vítima? ").lower()
    booleano_mora = None
    if pergunta_mora == 'sim':
        booleano_mora = True
    else:
        booleano_mora = False

    respostas.append(booleano_mora)


def devia():
    pergunta_devia = input("        Devia para a vítima? ").lower()
    booleano_devia = None
    if pergunta_devia == 'sim':
        booleano_devia = True
    else:
        booleano_devia = False

    respostas.append(booleano_devia)


def trabalhou():
    pergunta_trabalhou = input("        Já trabalhou com a vítima? ").lower()
    booleano_trabalhou = None
    if pergunta_trabalhou == 'sim':
        booleano_trabalhou = True
    else:
        booleano_trabalhou = False

    respostas.append(booleano_trabalhou)


telefonou()
local()
mora()
devia()
trabalhou()

print()
if respostas.count(True) < 2:
    print('                 Não suspeito')

if respostas.count(True) == 2:
    print('                 Suspeito')

if 3 <= respostas.count(True) <= 4:
    print('                 Cúmplice')

if respostas.count(True) == 5:
    print('                 Assassino!')
