altura = float(input('Diga sua altura (m): '))
sexo = int(input('Diga seu sexo (1:Mulher / 2:Homem): '))

if (sexo == 1):
    peso_ideal = 62.1 * altura - 44.7
else:
    peso_ideal = 72.7 * altura - 58

print(f'O seu peso ideal é de {peso_ideal:.2f}')
