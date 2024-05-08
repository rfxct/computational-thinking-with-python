def podeVotar(nome, idade):
    if idade >= 16:
        print(f'Sim, a pessoa {nome} pode votar')
        return True
    else:
        print(f'Não, a pessoa {nome} não pode votar')
        return False

a = podeVotar('Lucas', 18)
print(f'A primeira resposta foi {a}\n')

b = podeVotar('Maira', 13)
print(f'A segunda resposta foi {b}\n')

c = podeVotar('Pedro', 18)
print(f'A terceira resposta foi {c}\n')

