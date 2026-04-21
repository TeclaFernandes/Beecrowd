N = int(input())

num_retangulos = 0

while N != 0:

    gravetos = 0

    for i in range(N):
        Ci, Vi = map(int, input().split())
        if Vi % 2 != 0:
            Vi -= 1
        gravetos += Vi
    
    num_retangulos = gravetos // 4
    print(num_retangulos)

    N = int(input())
