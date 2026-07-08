from itertools import product

a, b, c = map(int, input().split())

valores = [a, b, c]

possivel = False

# escolhe usar ou não cada crédito e o sinal (+1 ou -1)
for escolhas in product([-1, 0, 1], repeat=3):
    # precisa usar pelo menos um crédito
    if escolhas == (0, 0, 0):
        continue

    soma = 0

    for i in range(3):
        soma += escolhas[i] * valores[i]

    if soma == 0:
        possivel = True
        break

print("S" if possivel else "N")