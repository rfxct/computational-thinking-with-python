preco_varejo = .30
preco_atacado = .25

total_macas = int(input('Digite quantas maçãs irá comprar: '))

if (total_macas < 12):
    valor_compra = total_macas * preco_varejo
else:
    valor_compra = total_macas * preco_atacado

print(f'O valor total da compra é de R${valor_compra:.2f}')
