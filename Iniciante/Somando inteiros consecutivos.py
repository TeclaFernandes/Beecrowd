valores = list(map(int, input().split()))

A = valores[0]

for N in valores[1:]:
    if N > 0:
        break

soma = 0

for i in range(N):
    soma += A + i

print(soma)