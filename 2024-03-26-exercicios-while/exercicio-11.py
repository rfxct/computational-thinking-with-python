'''
Faça um programa que peça um número inteiro e determine se ele é ou não um
número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''


num = int(input('Digite um número para testar\n> '))
i = num - 1
primo = True

while i > 1 or not primo:
    if (num % i) == 0:
        primo = False
        break

    i -= 1


print(f'O número {num} {"É" if primo else "NÃO É"} um número primo')
