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

'''
Escreva uma função que recebe um número e retorne True caso ele seja primo
'''
def numero_primo(num: int):
    for i in range(2, num):
        if num % i == 0:
            return False
    return False if num == 1 else True

'''
Escreva uma função que recebe um número, e devolve ua lista de todos os números primos até esse limite.
Se primos(100), retornaremos a lista de todos os primos menores que 100
'''
def primos(num: int):
   return [i for i in range(2, num) if numero_primo(i)]
