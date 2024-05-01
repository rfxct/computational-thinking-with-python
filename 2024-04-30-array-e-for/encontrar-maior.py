'''
6 - Encontrar o maior elemento da lista
'''

numeros = [3, 5, 13, 9, 2, 974, 322, 78, 43, 62]

maior = numeros[0]
for i in range(1, len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
print(f"O maior número encontrado foi: {maior}")
