'''
A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um
programa capaz de gerar a série até o n−ésimo termo.
'''


i = 0
n = int(input('Diga até qual posição você quer gerar a sequência\n> '))

(last, curr) = (1, 1)
resultado = f'{last},{curr}'

while i < (n - 2):
    (last, curr) = (curr, last + curr)
    resultado += f',{curr}'
    i += 1

print(f'Sequência: {resultado}')
