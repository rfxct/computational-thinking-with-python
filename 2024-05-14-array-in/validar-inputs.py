def verificar_numero(text: str, text_erro: str = 'O número digitado é inválido'):
    numero = input(text)
    while not numero.isnumeric():
        print(f'[ERRO] {text_erro}')
        numero = input(text)
    return int(numero)


quantidade = verificar_numero('Digite a quantidade de garrafas\n> ', 'Digite uma quantidade válida de garrafas')
idade = verificar_numero('Digite a sua idade\n> ', 'A idade deve ser um número inteiro')
