"""
Um funcionário de uma empresa recebe aumento salarial anualmente. Sabe-se que:
    1. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    2. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    3. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
    dobro do percentual do ano anterior. Faça um programa que determine o
    salário atual desse funcionário. Após concluir isto, altere o programa
    permitindo que o usuário digite o salário inicial do funcionário.
"""

ano_inicio = 1996
ano_fim = 2000
salario = ""
while not salario.isnumeric():
    salario = input("Digite o salário inicial do funcionário\n> ")
salario = int(salario)

porcentagem = 0.015

while ano_inicio < ano_fim:
    salario *= 1 + porcentagem
    ano_inicio += 1
    porcentagem *= 2

print(f"O salário final será de R$ {salario:.2f}")
