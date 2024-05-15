'''
Encontre o carro com o maior valor
'''

def buscar_posicao_maior(lista):
    idx_mais_caro = 0

    for i in range(1, len(lista)):
        if lista[i] > lista[idx_mais_caro]:
            idx_mais_caro = i
    return idx_mais_caro

carros = ['Fusca', 'Miata', 'Fox', 'Gol 1000']
precos = [8_000, 75_000, 16_000, 7_000]

idx_mais_caro = buscar_posicao_maior(precos)
print(f'O carro mais caro é o {carros[idx_mais_caro]}')

