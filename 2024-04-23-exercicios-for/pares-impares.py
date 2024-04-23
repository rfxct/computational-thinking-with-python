# Peça 10 números e diga a quantidade de pares e ímpares

pares = 0

for i in range(10):
    num = input(f'Digite o {i + 1}° número\n> ')
    while not num.isnumeric():
        num = input(f'Digite o {i + 1} número\n> ')

    if int(num) % 2 == 0:
        pares += 1
impares = i + 1 - pares
print(f'Você digitou {pares} PARES e {impares} ÍMPARES')
