op = input().strip()

mat = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    mat.append(linha)

soma = 0
cont = 0

for i in range(12):
    for j in range(12):
        if i > j and i + j > 11:
            soma += mat[i][j]
            cont += 1

if op == "S":
    print(f"{soma:.1f}")
else:
    print(f"{soma / cont:.1f}")