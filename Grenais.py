grenais = 0
inter_vitorias = 0
gremio_vitorias = 0
empates = 0

while True:
    i, g = map(int, input().split())

    grenais += 1

    if i > g:
        inter_vitorias += 1
    elif g > i:
        gremio_vitorias += 1
    else:
        empates += 1

    print("Novo grenal (1-sim 2-nao)")
    opcao = int(input())

    if opcao == 2:
        break

print(f"{grenais} grenais")
print(f"Inter:{inter_vitorias}")
print(f"Gremio:{gremio_vitorias}")
print(f"Empates:{empates}")

if inter_vitorias > gremio_vitorias:
    print("Inter venceu mais")
elif gremio_vitorias > inter_vitorias:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")