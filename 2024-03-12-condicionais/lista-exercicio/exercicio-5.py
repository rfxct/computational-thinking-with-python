valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo número: '))
valor3 = int(input('Digite o terceiro número: '))

if valor1 > valor3:
    maior = valor1
    valor1 = valor3
    valor3 = maior

if valor1 > valor2:
    maior = valor1
    valor1 = valor2
    valor2 = maior

if valor2 > valor3:
    maior = valor2
    valor2 = valor3
    valor3 = maior

print(f'{valor1}, {valor2}, {valor3}')
