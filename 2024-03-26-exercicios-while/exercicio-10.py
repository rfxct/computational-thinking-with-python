'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120
'''

i = res = num = int(input('Digite o número que você deseja calcular\n> '))
eq = str(i)

while i > 1:
    i -= 1

    eq += f'.{i}'
    res *= i


print(f'{num}! = {eq} = {res}')
