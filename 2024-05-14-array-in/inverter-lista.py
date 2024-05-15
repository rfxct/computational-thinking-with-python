'''
Construa uma função que receba uma lista e retorne ela invertida
'''

def inverter_lista(lista):
    ultimo = len(lista) - 1
    for i in range(len(lista) // 2):
        bkp = lista[i]

        lista[i] = lista[ultimo - i]
        lista[ultimo - i] = bkp

    return lista

invertida = inverter_lista([0, 1, 2, 3, 4, 5, 6])

print(f'A lista invertida é {invertida}')
