def validarTelefone(tel: str):
    is_valido = tel.isnumeric() and 8 <= len(tel) <= 11
    print(f'[!] O telefone {tel} tem {len(tel)} digitos e é {"VALIDO" if is_valido else "INVALIDO"}\n')

    return is_valido

telefone = input('Digite o telefone a ser testado\n> ')
while not validarTelefone(telefone):
    telefone = input('Digite o telefone a ser testado\n> ')
