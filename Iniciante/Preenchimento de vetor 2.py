t = int(input())
n = []

for i in range(1000):
    n.append(i % t)

for i in range(1000):
    print(f"N[{i}] = {n[i]}")