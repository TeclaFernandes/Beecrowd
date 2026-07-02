x = int(input())

# se for par, começa no próximo ímpar
if x % 2 == 0:
    x += 1

for i in range(6):
    print(x)
    x += 2