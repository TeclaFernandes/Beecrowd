N, C = map(int, input().split())

qntd_atual = 0
qntd_maxima = 'N'

for i in range(N):

    S, E = map(int, input().split())
    qntd_atual += E - S

    if qntd_atual > C :
        qntd_maxima = 'S'

print(qntd_maxima)