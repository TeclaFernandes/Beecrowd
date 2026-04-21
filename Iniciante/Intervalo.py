#([0,25], (25,50], (50,75], (75,100])
v = float(input())
if (v >= 0 and v <= 25):
     print("Intervalo [0,25]")
elif (v > 25 and v <= 50):
     print("Intervalo (25,50]")
elif (v > 50 and v <= 74): 
     print("Intervalo (50,75]")
elif (v > 75 and v <= 100):
     print("Intervalo (75,100]")
else: 
     print("Fora de intervalo")
