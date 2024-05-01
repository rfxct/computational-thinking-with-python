'''
7 - Crie uma lista com nomes de carros e uma lista com seus preços e printe o nome do carro mais caro
'''

carros = ['Gol 1000', 'Haval', 'Corcel', 'Taos', 'Lancer', 'Palio']
precos = [14_500, 214_000, 22_000, 155_000, 69_000, 22_000]

posicao_maior = 0
for i in range(1, len(carros)):
    if precos[i] > precos[posicao_maior]:
        posicao_maior = i

print(f'O carro mais caro é o {carros[posicao_maior]}, custando R$ {precos[posicao_maior]}')
