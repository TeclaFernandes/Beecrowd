x = int(input())

z = int(input())
while z <= x:
    z = int(input())

soma = 0
cont = 0
valor = x

while soma <= z:
    soma += valor
    valor += 1
    cont += 1

print(cont)