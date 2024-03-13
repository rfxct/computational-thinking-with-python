angulo1 = int(input('Digite o tamanho do primeiro ângulo: '))
angulo2 = int(input('Digite o tamanho do segundo ângulo: '))
angulo3 = int(input('Digite o tamanho do terceiro ângulo: '))

if angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print('Triângulo Obtusângulo')
elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print('Triângulo Retângulo')
else:
    print('Triângulo Acutângulo')
