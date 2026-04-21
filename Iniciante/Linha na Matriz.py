import numpy as np

M = np.zeros((12,12), dtype=float)
L = int(input())
T = input().upper()

soma = 0
cont = 0

for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        M[i][j] = float(input())
        if i == L:
            soma += M[i][j]
            cont += 1
            
if T == 'S':
    print(f'{soma:.1f}')
elif T == 'M':
    print(f'{(soma/cont):.1f}')