'''
a cada ano a populacao de um pais dobra, este pais comeca com 100 mil pessoas. quantos anos a populacao atingira 1 bilhao?
'''

populacao = 1e5 # 100_000
anos = 0

while populacao < 1e9: # 1_000_000_000
    populacao *= 2
    anos += 1

print(f'Levará {anos} anos para a população chegar a 1 bilhão')
