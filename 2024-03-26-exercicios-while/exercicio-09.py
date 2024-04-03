'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
números pares e a quantidade de números ímpares.
'''

(i, par, impar) = (0, 0, 0)

while i < 10:
    i += 1
    n = int(input(f'Forneça o {i}° número: '))

    if n % 2:
        impar += 1
    else:
        par += 1

print(f'Você digitou {par} PARES e {impar} ÍMPARES')
