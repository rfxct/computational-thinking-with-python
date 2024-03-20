total_lados = int(input('Diga quantos lados tem o polígono: '))

if total_lados < 3:
    print('NÃO É UM POLÍGONO')
elif (total_lados > 5):
    print('POLÍGONO NÃO IDENTIFICADO')
else:
    medida_lado = int(input('Diga a medida do lado do polígono: '))

    if total_lados == 3:
        forma = print('A figura é um triângulo')
    elif total_lados == 4:
        print('A figura é um quadrado')
    else:
        print('A figura é um pentágono')

    perimetro = total_lados * medida_lado
    print(f'A figura é um {forma}')
    print(f'O perímetro do objeto é {perimetro}')



