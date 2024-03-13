'''
Velocidade entre 100 e 120 multa de V * 20%
Velocidade entre 120 e 150 multa de 120 * 20% + V * 30%
Velocidade acima de 150 multa de 120 * 20% + 150 * 30% + V*40%
'''

velocidade = int(input('Diga a velocidade utilizada: '))

multa = 0

if velocidade >= 100 and velocidade <= 120:
    print()
elif velocidade > 120 and velocidade <= 150:
    print()
elif velocidade > 150:
    print()
