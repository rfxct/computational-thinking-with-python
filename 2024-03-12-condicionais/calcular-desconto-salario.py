salario = float(input("Diga seu salário : "))

if salario <= 1903.98:
    aliquota = 0
elif salario <= 2826.65:
    aliquota = 7.5 / 100
elif salario <= 3751.05:
    aliquota = 15 / 100
elif salario <= 4664.68:
    aliquota = 22.5 / 100
else:
    aliquota = 27.5 / 100

desconto = aliquota * salario
salario -= desconto

print(f"Seu salário será de {salario}")
