texto = input('Digite a string que você deseja saber o tamanho\n> ')
length = 0

for letra in texto:
    length += 1
print(f'A string "{texto}" tem {length} caracteres')
