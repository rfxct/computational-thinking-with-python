'''
Escreva uma funçâo que receba um número, e retorna uma lista de strings que representa a tabuada desse número (ex: tabuada_do(3))
retorna ['3x1=3', '3x2=6']
'''

def tabuada_do(num: int):
    return [f'{num}x{i}={i * num}' for i in range(1, 11)]

'''
Escreva uma função que retorne uma lista com todas as tabuadas, do 1 ao 10
'''

def gerar_tabuadas():
    tabuadas = []

    for i in range(1, 11):
        tabuadas.append(tabuada_do(i))
    return tabuadas
