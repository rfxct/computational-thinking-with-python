def buscar_mais_caro(carros, precos):
    idx_mais_caro = 0

    for i in range(1, len(precos)):
        if precos[i] > precos[idx_mais_caro]:
            idx_mais_caro = i
    return (carros[idx_mais_caro], precos[idx_mais_caro])

carros = ['Uno', 'Toro', 'Gol 1000']
precos = [13_000, 120_000, 7_000]

(nome_carro, valor_carro) = buscar_mais_caro(carros, precos)

print(f'{nome_carro} é o mais caro e custa R$ {valor_carro:.2f}')
