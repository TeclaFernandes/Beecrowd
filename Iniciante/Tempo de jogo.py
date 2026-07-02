inicio, fim = map(int, input().split())

if fim > inicio:
    duracao = fim - inicio
elif fim < inicio:
    duracao = (24 - inicio) + fim
else:
    duracao = 24

print(f"O JOGO DUROU {duracao} HORA(S)")