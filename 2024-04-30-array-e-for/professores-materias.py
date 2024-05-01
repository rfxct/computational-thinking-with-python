'''
4 - Faça uma lista com seus professores e uma lista com as materias dos seus professores,
    em ordem printe "O professor X dá aula de Y"
'''

professores = ['Danilo', 'Demetrius', 'Caio']
materias = ['Computational Thinking With Python', 'Edge Computing and Computer Systems', 'Web Development']

for i in range(len(professores)):
    print(f"O professor {professores[i]} dá aula de {materias[i]}")
