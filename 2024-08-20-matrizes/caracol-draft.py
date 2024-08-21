'''
* - * * * * *
* - * - - - *
* - * - * - *
* - * * * - *
* - - - - - *
* * * * * * *

  0 1 2 3 4 5 6 7 8
0 * - * * * * * * *
1 * - * - - - - - *
2 * - * - * * * - *
3 * - * - * - * - *
4 * - * - - - * - *
5 * - * * * * * - *
6 * - - - - - - - *
7 * * * * * * * * *
'''
import math

def criar_matriz(altura, largura):
    matriz = []
    for _ in range(altura):
        linha = ['-' for _ in range(largura)]
        matriz.append(linha)
    return matriz

def monta_matriz(matriz):
    resultado = ''

    for linha in matriz:
        for char in linha:
            resultado += char
        resultado += '\n'
    return resultado

char_estrela, char_hifen = '*', '-'
def caracol(altura):
    largura = altura + 1
    matriz = criar_matriz(altura, largura)

    ml, mc = math.floor(altura / 2), math.floor(largura / 2)

    pl, pc = 0, 0

    matriz[pl][pc] = char_estrela
    matriz[ml][mc] = char_estrela

    while (
        pl != ml or pc != mc
    ):
        matriz[pl][pc] = char_estrela

        pl += -1 if pl == altura - 1 else 1

        # if pl > 0 and matriz[pl - 1][pc] == char_estrela:
        #     matriz[pl][pc] = char_estrela
        # # if matriz[pl - 1] == char_estrela and len(matriz)
        # pl += 1
        # if pl == altura and :
        #     break

    return matriz

# Teste
print(
    monta_matriz(caracol(8))
)
