senha_cadastrada = '1234'
for i in range(3):
    senha = input('Digite a senha a ser testada\n> ')
    if senha == senha_cadastrada:
        print('Login efetuado com sucesso')
        break
    print(f'Você só tem mais {2-i} tentativas')

if senha != senha_cadastrada:
    print('Acesso negado')
