lado1 = int(input('Digite o tamanho do primeiro lado: '))
lado2 = int(input('Digite o tamanho do segundo lado: '))
lado3 = int(input('Digite o tamanho do terceiro lado: '))

if (lado1 == lado2 and lado2 == lado3):
    print('O triângulo é Equilátero')
elif (lado1 == lado2 or lado2 == lado3 or lado1 == lado3):
    print('O triângulo é Isósceles')
else:
    print('O triângulo é Escaleno')
