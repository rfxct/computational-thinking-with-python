'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a
tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
'''

i = 1
multiplicador = int(input('Digite o número que você deseja ver a tabuada\n> '))

while i <= 10:
    print(f'{multiplicador} x {i} = {multiplicador * i}')
    i += 1
