'''
Peça ao usuario um professor de input
Verifique se esse professor esta na lista
printe o que o professor escolhido dá
se não estiver na lista, mande o usuario digitar novamente
'''

professores = ['Cordeiro', 'Danilo', 'Lucas Silva', 'Lucas Augusto', 'Jones', 'Ana Claudia', 'Caio Ribeiro']
materias = ['Sw & Tx', 'Python', 'Front', 'Edge', 'Matemática', 'Story', 'Web']

professor_escolhido = input('Digite o nome de um professor\n> ')
while professor_escolhido not in professores:
    print('\n[ERRO] O professor escolhido não é válido')
    professor_escolhido = input('Digite o nome de um professor\n> ')

for i, prof in enumerate(professores):
    if prof == professor_escolhido:
        print(f'O prof. {prof} dá a matéria {materias[i]}')
        break
