'''
Faça um programa que leia 5 números e informe a soma e a média dos números
'''

i = 0
soma = 0
media = 0

while i < 5:
    i += 1
    soma += int(input(f'Forneça o {i}° número: '))

media = soma / i

print(f'A soma dos números é: {soma}')
print(f'A média dos números é {media}')
