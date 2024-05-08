def maiorNumeroLista(numeros):
    maior = numeros[0]

    for i in range(1, len(numeros)):
        if numeros[i] > maior:
            maior = numeros[i]

    return maior

n = maiorNumeroLista([10, 20, 2, 30, 7])
print(f'O PRIMEIRO maior número digitado foi {n}')

n2 = maiorNumeroLista([100, 200, 2, 30, 7])
print(f'O SEGUNDO maior número digitado foi {n2}')


n3 = maiorNumeroLista([-2, -3, -1])
print(f'O TERCEIRO maior número digitado foi {n3}')
'''
numeros = []
for i in range(5):
    num = input(f'Digite o {i + 1}° número\n> ')
    while not num.isnumeric():
        print('[ERRO] O número deve ser inteiro')
        num = input(f'Digite o {i + 1}° número\n> ')
    num = int(num)
    numeros.append(num)
'''
