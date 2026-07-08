n = int(input())

for _ in range(n):
    h, m, o = map(int, input().split())

    if o == 1:
        print(f"{h:02d}:{m:02d} - A porta abriu!")
    else:
        print(f"{h:02d}:{m:02d} - A porta fechou!")