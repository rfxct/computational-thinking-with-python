def proximoMinuto(hora, minuto):
    if minuto == 59:
        if hora == 23:
            hora = 0
        else:
            hora + 1
        minuto = 0
    else:
        minuto += 1
    return f'{hora}h{str(minuto).zfill(2)}'

h1 = proximoMinuto(22, 59)
print(f'[H1] A hora acrescida em 1 minuto é: {h1}')

h2 = proximoMinuto(12, 3)
print(f'[H2] A hora acrescida em 1 minuto é: {h2}')

h3 = proximoMinuto(23, 59)
print(f'[H3] A hora acrescida em 1 minuto é: {h3}')

