import numpy as np

N = int(input())
vetor_bool = np.zeros(N, dtype=int)
vetor_minas = np.zeros(N, dtype=int)

for i in range(N):
    vetor_bool[i] = input()

for i in range(len(vetor_bool)):

    if vetor_bool[i] == 1:
        vetor_minas[i] += 1
        if i-1 >= 0:
            vetor_minas[i-1] += 1
        if i+1 < len(vetor_minas):
            vetor_minas[i+1] += 1
            
for mina in vetor_minas:
    print(mina)