"""
Em uma eleição presidencial existem quatro candidatos. Os votos são informados
por meio de código. Os códigos utilizados são:
1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o
conjunto de votos tem-se o valor zero.
"""

(sair, jose, joao, lucia, marina, nulo, branco) = ("0", "1", "2", "3", "4", "5", "6")
(tt_jose, tt_joao, tt_lucia, tt_marina, tt_nulo, tt_branco, i) = (0, 0, 0, 0, 0, 0, 0)

menu = (
    f"\n{jose} - José\n"
    + f"{joao} - João\n"
    + f"{lucia} - Lúcia\n"
    + f"{marina} - Marina\n"
    + f"{branco} - Branco\n"
    + f"{nulo} - Nulo\n"
    + f"{sair} - Sair\n"
    + "> "
)

while True:
    voto = input(menu)
    while (
        voto != jose
        and voto != joao
        and voto != lucia
        and voto != marina
        and voto != nulo
        and voto != branco
        and voto != sair
    ):
        print('\nVoto inválido. Digite de acordo com o menu abaixo:')
        voto = input(menu)

    if voto == sair:
        break
    elif voto == jose:
        tt_jose += 1
    elif voto == joao:
        tt_joao += 1
    elif voto == lucia:
        tt_lucia += 1
    elif voto == marina:
        tt_marina += 1
    elif voto == branco:
        tt_branco += 1
    elif voto == nulo:
        tt_nulo += 1
    i += 1

print(
    f"Total José: {tt_jose}\n"
    + f"Total João: {tt_joao}\n"
    + f"Total Lúcia: {tt_lucia}\n"
    + f"Total Marina: {tt_marina}\n"
    + f"Total Branco: {tt_branco}\n"
    + f"Total Nulo: {tt_nulo}\n\n"
    + f"Nulos sobre Total: {tt_nulo/i:.2f}%\n"
    + f"Brancos sobre Total: {tt_branco/i:.2f}%"
)