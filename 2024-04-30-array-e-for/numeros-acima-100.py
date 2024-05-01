'''
5 - Peça 10 números ao usuário e guarde numa lista inicialmente vazia, depois conte quantos estão acima de 100
'''

numeros = []

for i in range(10):
    num = input(f'Digite o {i + 1}° número\n> ')
    while not num.isnumeric():
        print('[ERRO] Você forneceu um número inválido')
        num = input(f'Digite o {i + 1}° número\n> ')
    numeros.append(int(num))

total_acima_100 = 0
for num in numeros:
    if num > 100:
        total_acima_100 += 1
print(f'Você digitou {total_acima_100} números maiores que 100')
