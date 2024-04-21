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

'''
# Solução Danilo utilizando raiz
num = 31
i = 2
while i < num**0.5:
    print(f"{num}%{i} = {num%i}")
    if num%i == 0:
        print(f"{num} não é primo")
        break
    i+=1
if i >= num**0.5:
    print(f"{num} é primo")
'''