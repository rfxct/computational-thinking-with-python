'''
2 - Declare uma lista com 10 numeros dentro encontre a soma e a media dos numeros ali contidos
'''

numeros = [2, 7, 9, 54, 32, 65, 78, 99, 105]
soma = 0
for num in numeros:
    soma += num
print(f"A soma dos números é {soma} e a média é {soma/len(numeros):.2f}")
