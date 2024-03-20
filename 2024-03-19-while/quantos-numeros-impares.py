numero1 = int(input('Digite o primeiro um número: '))
numero2 = int(input('Digite o segundo um número: '))
numero3 = int(input('Digite o terceiro um número: '))
numero4 = int(input('Digite o quarto um número: '))
numero5 = int(input('Digite o quinto um número: '))


impares = 0

if numero1 % 2:
    impares += 1

if numero2 % 2:
    impares += 1

if numero3 % 2:
    impares += 1

if numero4 % 2:
    impares += 1

if numero5 % 2:
    impares += 1

print(f'Você escreveu {5 - impares} números pares e {impares} números ímpares')
