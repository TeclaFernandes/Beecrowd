valores_validos = 0
soma = 0.0

while valores_validos < 2:
    nota = float(input())

    if 0 <= nota <= 10:
        soma += nota
        valores_validos += 1
    else:
        print("nota invalida")

media = soma / 2
print(f"media = {media:.2f}")