'''
1 - Declare uma lista com 10 números dentro e conte a quantidade de números pares e impares lá dentro
'''


numeros = [3, 6, 1, 9, 53, 17, 92, 2, 41, 2]
impares = 0

for num in numeros:
    if num % 2:
        impares += 1

print(f"Há {impares} números ÍMPARES e {len(numeros) - impares} números PARES")
