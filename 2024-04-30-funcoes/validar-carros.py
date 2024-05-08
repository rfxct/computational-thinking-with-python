def validarCarro(carros):
    nome_carro = input('Digite o nome do carro a ser testado\n> ')

    for carro in carros:
        if carro.lower() == nome_carro.lower():
            print('[+] O carro digitado está na lista')
            return True
    print('[-] O carro digitado é INVALIDO')
    return False

validarCarro([
    'Miata',
    'Gol 1000',
    'Lancer',
    'Kadett'
])
