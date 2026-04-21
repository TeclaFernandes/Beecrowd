Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())

cont = 0
if (Ca and Ba and Pa and Cr and Br and Pr) >= 0 and (Ca and Ba and Pa and Cr and Br and Pr) <= 100:
    if Cr > Ca: 
        cont += Cr - Ca
    if Br > Ba:
        cont += Br - Ba
    if Pr > Pa:
        cont += Pr - Pa
print(cont)