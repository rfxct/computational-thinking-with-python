'''
Crie uma função que recebe uma lista e um elemento a ser buscado, e retorna a posição desse elemento na lista
'''

def buscar_posicao(lista, busca):
    for i, el in enumerate(lista):
        if el == busca:
            return i
    return -1

carros = ['Kadett', 'Gol', 'Chevette', 'Lancer']
elemento = input('Digite o carro a ser buscado\n> ')

while elemento not in carros:
    print('\n[ERRO] Digite um carro presente na lista')
    elemento = input('Digite o carro a ser buscado\n> ')

posicao = buscar_posicao(carros, elemento)
print(f'A posição do elemento na lista é: {posicao}')
