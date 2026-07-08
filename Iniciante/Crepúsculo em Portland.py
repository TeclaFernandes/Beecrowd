n = int(input())

mapa = []

for _ in range(n + 1):
    mapa.append(list(map(int, input().split())))

for i in range(n):
    linha = ""

    for j in range(n):
        cameras = (
            mapa[i][j] +
            mapa[i][j + 1] +
            mapa[i + 1][j] +
            mapa[i + 1][j + 1]
        )

        if cameras >= 2:
            linha += "S"
        else:
            linha += "U"

    print(linha)