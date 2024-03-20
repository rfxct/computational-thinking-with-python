i = 0
impares = 0

while (i < 10):
    i += 1
    numero = int(input(f'Digite o {i}° número: '))
    if numero % 2:
        impares += 1

print(f'Você digitou {i - impares} números pares e {impares} ímpares')
