"""
Faça um programa que leia uma quantidade indeterminada de números positivos e
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.
"""

int0_25 = 0
int26_50 = 0
int51_75 = 0
int76_100 = 0

while True:
    num = int(input("Digite o número a ser testado\n> "))
    if num < 0:
        break

    if num <= 25:
        int0_25 += 1
    elif num <= 50:
        int26_50 += 1
    elif num <= 75:
        int51_75 += 1
    elif num <= 100:
        int76_100 += 1

print(f"Intervalo [0-25]: {int0_25}")
print(f"Intervalo [26-50]: {int26_50}")
print(f"Intervalo [51-76]: {int51_75}")
print(f"Intervalo [76-100]: {int76_100}")
