count = 0

for _ in range(5):
    x = int(input())
    if x % 2 == 0:
        count += 1

print(f"{count} valores pares")