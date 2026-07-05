while True:
    n = int(input())
    if n == 0:
        break

    max_val = 2 ** (2 * n - 2)
    t = len(str(max_val))

    for i in range(n):
        linha = []
        for j in range(n):
            valor = 2 ** (i + j)
            linha.append(f"{valor:>{t}}")

        print(" ".join(linha))

    print()