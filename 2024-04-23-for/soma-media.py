# Peça 10 números para o usuário e diga a soma e a média dos números

soma = 0

for i in range(10):
    num = input(f'Digite o {i + 1}° número\n> ')
    while not num.isnumeric():
        num = input(f'Digite o {i + 1} número\n> ')
    soma += int(num)

print(
    f'A soma dos números é {soma}\n'
    f'A média dos números é {soma/(i+1)}'
)
