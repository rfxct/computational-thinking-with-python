'''
Faça um programa que calcule o mostre a média aritmética de N notas.
'''

i = 0
qtd = int(input('Digite quantas notas serâo inseridas\n> '))
soma = 0

while i < qtd:
    i += 1
    soma += int(input(f'Forneça o {i}° número: '))

media = soma / qtd

print(f'A média dos números é {media}')
