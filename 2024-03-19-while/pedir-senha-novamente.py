senha_cadastrada = '1234'
senha = input('Digite a senha: ')
tentativas = 3

while senha != senha_cadastrada and tentativas:
    senha = input(f'Senha incorreta. Você pode tentar mais {tentativas} vezes: ')
    tentativas -= 1

if senha == senha_cadastrada:
    print('\nLogin efetuado')
else:
    print('\nVocê errou sua senha muitas vezes')
