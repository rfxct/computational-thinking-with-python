def tabuleiro_xadrez(tamanho):
    matriz = []

    for lin in range(tamanho):
        linha = []

        for col in range(tamanho):
            linha.append('x' if (col + lin) % 2 else '.')
        matriz.append(linha)

    return matriz
