# Entrada de dados: número de funcionários por andar
A1 = int(input())  # número de funcionários no 1º andar
A2 = int(input())  # número de funcionários no 2º andar
A3 = int(input())  # número de funcionários no 3º andar

# Cálculo do tempo total para cada posicionamento da máquina
primeiro_andar = A2 * 2 + A3 * 4
segundo_andar = A1 * 2 + A3 * 2
terceiro_andar = A1 * 4 + A2 * 2

# Encontrar o mínimo dos tempos calculados
menor_tempo = min(primeiro_andar, segundo_andar, terceiro_andar)

# Saída do resultado
print(menor_tempo)