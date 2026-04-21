import math

# Lê os valores dos pontos p1 e p2
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# Calcula a distância entre os pontos
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Exibe o resultado com 4 casas decimais
print(f'{distancia:.4f}')