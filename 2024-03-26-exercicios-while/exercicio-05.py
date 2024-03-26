'''
Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles
'''

num = int(input('Forneça o PRIMEIRO número do intervalo: '))
maximo = int(input('Forneça o SEGUNDO número do intervalo: '))

if num > maximo:
    (num, maximo) = (maximo, num)


while num < maximo - 1:
    num += 1
    print(num)
