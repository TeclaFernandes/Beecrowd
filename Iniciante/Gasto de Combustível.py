#RECEBENDO O TEMPO E A VEOCIDADE GASTOS NA VIAGEM:
tempo = int(input())
velocidade = int(input())

#DESCOBRINDO A DISTANCIA:
distancia = tempo * velocidade

#CALCULANDO O COMBUSTIVEL:
combustivel = distancia / 12

#IMPRIMINDO A QUANTIDADE DE LITROS NESCESSARIAS:
print(f'{combustivel:.3f}')