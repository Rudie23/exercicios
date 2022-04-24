"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
uma mensagem de erro e voltando a pedir as informações."""
nome = ''
senha = None
while True:
    try:
        nome = input('Digite um nome para um usuário: ')
        senha = input('Crie uma senha: ')

    except nome == senha:
        print('O usuário e senha devem ser diferentes')
    else:
        if nome != senha:
            break

print('Usuário e senha criados com sucesso.')
print(f'Usuário é {nome}!')
print(f'A senha é {senha}!')
