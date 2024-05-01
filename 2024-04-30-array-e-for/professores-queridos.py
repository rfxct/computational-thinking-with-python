'''
3 - Declare uma lista com o nome dos seus professores queridos, vverifique se o Danilo está ali dentro,
    caso ele esteja, printe a casa em que foi encontrado e também "O Danilo é querido"
'''

professores = ['Caio', 'Demetrius', 'Danilo', 'Lucas',  'Cordeiro']

for i in range(len(professores)):
    if professores[i] == 'Danilo':
        print(f'O Danilo é querido e foi encontrado no índice {i}')
        break

for i, professor in enumerate(professores):
    if professor == 'Danilo':
        print(f'O Danilo é querido e foi encontrado no índice {i}')
        break
