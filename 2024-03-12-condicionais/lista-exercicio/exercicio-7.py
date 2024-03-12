total_lados = int(input('Diga quantos lados tem o polígono: '))
medida_lado = int(input('Diga a medida do lado do polígono: '))

if (total_lados == 3):
    print('A figura é um triângulo')
if total_lados == 4:
    print('A figura é um quadrado')
if total_lados == 5:
    print('A figura é um pentágono')

perimetro = total_lados * medida_lado
print(f'O perímetro do objeto é {perimetro}')
