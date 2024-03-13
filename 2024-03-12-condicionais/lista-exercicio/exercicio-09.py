valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo número: '))
valor3 = int(input('Digite o terceiro número: '))

maior_valor = valor1

if valor3 > valor2 and valor3 > valor1:
    maior_valor = valor3
elif valor2 > valor3 and valor2 > valor1:
    maior_valor = valor2

print(f'O maior valor é {maior_valor}')
