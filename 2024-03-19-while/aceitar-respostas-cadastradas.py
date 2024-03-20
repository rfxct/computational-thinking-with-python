'''
# Versão com AND
resposta = input('Digite sua resposta (sim/não): ')

while (resposta != 'sim' and resposta != 'não'):
    resposta = input('Resposta inválida. Digite novamente (sim/não): ')
print('Resposta aceita')
'''

# Versão com OR
resposta = input('Digite sua resposta (sim/não): ')
while not (resposta == 'sim' or resposta == 'não'):
    resposta = input('Resposta inválida. Digite novamente (sim/não): ')
print('Resposta aceita')

