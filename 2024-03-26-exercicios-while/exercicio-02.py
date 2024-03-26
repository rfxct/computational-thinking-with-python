'''
Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
'''

nome = ''
idade = 0
salario = 0
sexo = ''
estado_civil = ''

while (
        (len(nome) <= 3) or
        (idade <= 0 or idade >= 150) or
        (salario <= 0) or
        not (sexo == 'f' or sexo == 'm') or
        not (
            estado_civil == 's' or
            estado_civil == 'c' or
            estado_civil == 'v' or
            estado_civil == 'd'
        )
):
    if len(nome) <= 3:
        nome = input('Digite seu nome (min. 4 letras): ')

    if idade <= 0 or idade >= 150:
        idade = int(input('Digite sua idade (entre 0 e 150): '))

    if salario <= 0:
        salario = float(input('Digite seu salário (maior que 0): '))

    if sexo != 'f' and sexo != 'm':
        sexo = input('Digite seu sexo (f/m): ')

    if (
            estado_civil != 's' and
            estado_civil != 'c' and
            estado_civil != 'v' and
            estado_civil != 'd'
    ):
        estado_civil = input('Digite seu estado civil (s/c/v/d): ')


print('\nInformações validadas:\n',
      f'Nome: {nome}\n',
      f'Idade: {idade}\n',
      f'Salário: {salario}\n',
      f'Sexo (f/m): {sexo}\n',
      f'Estado Civil (s/c/v/d): {estado_civil}',
)
