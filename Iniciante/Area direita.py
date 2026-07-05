op = input().strip()

soma = 0
cont = 0

for i in range(12):
    for j in range(12):
        x = float(input())

        if i < j and i + j > 11:
            soma += x
            cont += 1

if op == "S":
    print(f"{soma:.1f}")
else:
    print(f"{soma / cont:.1f}")