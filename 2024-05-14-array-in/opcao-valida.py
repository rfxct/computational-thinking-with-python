'''
Faça uma função que recebe uma lista de opções válidas e obrigue o usuário a fornecer uma opção presente na lista
'''

def verificar_opcao(opcoes_validas, text, text_erro):
    opcao_escolhida = input(f'{text}\n> ')

    if opcao_escolhida not in opcoes_validas:
        print(f'\n[ERRO] {text_erro}')
        verificar_opcao(opcoes_validas, text, text_erro)


vinhos = ['Dom Bosco', 'Gato Negro', 'Pérgola', 'Cantinho do Vale']
verificar_opcao(vinhos, 'Digite o nome de um vinho', 'O vinho fornecido é inválido')
