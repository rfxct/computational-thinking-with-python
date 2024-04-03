'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
pedir as informações.
'''

(username, password) = ('', '')

while username == password:
    print('\nForneça uma senha diferente do nome de usuário')

    username = input('Digite o seu nome de usuário: \n> ')
    password = input('Digite sua senha: \n> ')

print('Acesso liberado')
