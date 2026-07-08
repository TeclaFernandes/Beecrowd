n = int(input())

valor = 0.0

for _ in range(n):
    valor = 1 / (2 + valor)

resultado = 1 + valor

print(f"{resultado:.10f}")