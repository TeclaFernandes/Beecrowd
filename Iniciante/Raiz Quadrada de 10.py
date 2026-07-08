n = int(input())

valor = 0.0

for _ in range(n):
    valor = 1 / (6 + valor)

resultado = 3 + valor

print(f"{resultado:.10f}")