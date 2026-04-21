# Lê os três valores de entrada
A, B, C = map(float, input().split())

# Calcula as áreas
area_triangulo = (A * C) / 2
area_circulo = 3.14159 * C**2
area_trapezio = ((A + B) * C) / 2
area_quadrado = B**2
area_retangulo = A * B

# Exibe as áreas com 3 dígitos após o ponto decimal
print(f'TRIANGULO: {area_triangulo:.3f}')
print(f'CIRCULO: {area_circulo:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')