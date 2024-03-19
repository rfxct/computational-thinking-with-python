# ate 100 sem multa
# ate 120 -> 20% * V
# ate 150 -> 120 * 20% + 30% * v
# mais de 150 -> 120 * 20% + 150 * 30% + 40% * v

while True:
    velocidade = int(input('Digite a velocidade: '))
    multa = 0

    # Jeito 1
    if (velocidade > 100):
        multa += .2 * (120 if velocidade >= 120 else velocidade)

    if (velocidade > 120):
        multa += .3 * (150 if velocidade >= 150 else velocidade)

    if (velocidade > 150):
        multa += .4 * velocidade
    print(f'[Jeito 1] O valor da multa é de R${multa:.2f}')

    # Jeito 2
    multa = 0

    if velocidade > 100 and velocidade <= 120:
        multa = velocidade * .2
    elif velocidade > 120 and velocidade <= 150:
        multa = 120 * .2 + velocidade * .3
    elif velocidade > 150:
        multa = 120 * .2 + 150 * .3 + velocidade * .4
    print(f'[Jeito 2] O valor da multa é de R${multa:.2f}')

    # Jeito 3 (Danilo)
    multa = 0

    if velocidade <= 100:
        multa = 0
    elif velocidade <= 120:
        multa = velocidade * .2
    elif velocidade <= 150:
        multa = 120 * .2 + velocidade * .3
    else:
        multa = 120 * .2 + 150 * .3 + velocidade * .4
    print(f'[Jeito 3] O valor da multa é de R${multa:.2f}')

