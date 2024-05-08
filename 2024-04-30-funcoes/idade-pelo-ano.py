def idadePeloAno(ano):
    return 2024 - ano

ano_nascimento = input('Digite o ano de nascimento\n> ')
while not ano_nascimento.isnumeric() or len(ano_nascimento) != 4:
    print('[ERRO] Ano deve ser um inteiro de 4 dígitos')
    ano_nascimento = input('Digite o ano de nascimento\n> ')

ano_nascimento = int(ano_nascimento)
idade = idadePeloAno(ano_nascimento)

print(f'[!] Você tem {idade} anos')

# Com array
pessoas = [
    ['Marcos', 2003],
    ['Alex', 2005]
]

for (nome, ano_nascimento) in pessoas:
    idade = idadePeloAno(ano_nascimento)
    print(f'[+] {nome} tem {idade} anos')
