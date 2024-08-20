'''
Escreva uma função que recebe um número e retorne True caso ele seja primo
'''
def numero_primo(num: int):
    for i in range(2, num):
        if num % i == 0:
            return False
    return not num == 1

'''
Escreva uma função que recebe um número, e devolve ua lista de todos os números primos até esse limite.
Se primos(100), retornaremos a lista de todos os primos menores que 100
'''
def primos(num: int):
   return [i for i in range(2, num) if numero_primo(i)]
