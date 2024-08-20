from math import ceil
'''
Faça uma função palindromo, que recebe uma string e responde True se ela é um palindromo,
False caso contrário. Palindromo é uma string espelhada. palindromo(“aba”) deve retornar True
palindromo(“abacate”) deve retornar false
'''

def palindromo(value: str):
    lastIdx = len(value) - 1

    for i in range(0, ceil(lastIdx / 2)):
        j = lastIdx - i
        if value[j] != value[i]:
            return False
    return True

'''
Faça uma função maior palindromo, que retorna o maior palindromo que podemos achar, 
considerando o começo de uma string. Por exemplo, maior_palindromo(‘abacate’) deve retornar ‘aba’ 
'''

def maior_palindromo(value: str):
    while not palindromo(value) and len(value):
        value = value[:-1]
    return value