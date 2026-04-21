# Lê os três valores de entrada
A, B, C = map(float, input().split())

maiorAB = (A+B+abs(A-B))/2
if maiorAB > C:
    print(f'{int(maiorAB)} eh o maior')
else: 
    print(f'{int(C)} eh o maior')