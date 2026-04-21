import math

A, B, C = map(float, input().split())
# print(A)
delta = B**2-4*A*C
if delta >= 0 and (2*A!=0):
    R1 = (B*(-1)+math.sqrt(delta))/(2*A)
    R2 = (B*(-1)-math.sqrt(delta))/(2*A)
    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')
else:
    print('Impossivel calcular')