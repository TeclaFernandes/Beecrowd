par = impar = positivo = negativo = 0

for _ in range(5):
    x = int(input())

    if x % 2 == 0:
        par += 1
    else:
        impar += 1

    if x > 0:
        positivo += 1
    elif x < 0:
        negativo += 1

print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(s)")
print(f"{negativo} valor(es) negativo(s)")