soma = 0
quantidade = 0

while True:
    idade = int(input())

    if idade < 0:
        break

    soma += idade
    quantidade += 1

media = soma / quantidade

print(f"{media:.2f}")