# Faça a tabuada de todos os números de 1-10 usando for's

for i in range(1, 11, 1):
    print(f'\n------------------\nTabuada do {i}\n------------------\n')

    for j in range(1, 11, 1):
        print(f'{i} x {j} = {i * j}')
