a, b, c = map(float, input().split())

# ordenar em ordem decrescente
x, y, z = sorted([a, b, c], reverse=True)

# primeiro: verifica se forma triângulo
if x >= y + z:
    print("NAO FORMA TRIANGULO")
else:
    x2 = x * x
    y2 = y * y
    z2 = z * z

    if x2 == y2 + z2:
        print("TRIANGULO RETANGULO")
    elif x2 > y2 + z2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    # tipos adicionais
    if x == y == z:
        print("TRIANGULO EQUILATERO")
    elif x == y or x == z or y == z:
        print("TRIANGULO ISOSCELES")