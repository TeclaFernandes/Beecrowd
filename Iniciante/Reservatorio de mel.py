import sys

pi = 3.14

valores = sys.stdin.read().split()

for i in range(0, len(valores), 2):
    v = float(valores[i])
    d = float(valores[i + 1])

    r = d / 2

    area = pi * r * r
    altura = v / area

    print(f"ALTURA = {altura:.2f}")
    print(f"AREA = {area:.2f}")