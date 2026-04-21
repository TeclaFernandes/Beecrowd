# Lê o valor inteiro (tempo em segundos)
tempo_em_segundos = int(input())

# Calcula as horas, minutos e segundos
horas = tempo_em_segundos // 3600
tempo_em_segundos %= 3600
minutos = tempo_em_segundos // 60
segundos = tempo_em_segundos % 60

# Exibe o resultado no formato horas:minutos:segundos
print(f'{horas}:{minutos}:{segundos}')