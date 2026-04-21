# Lê o valor inteiro (idade em dias)
idade_em_dias = int(input())

# Calcula os anos
anos = idade_em_dias // 365
idade_em_dias %= 365

# Calcula os meses
meses = idade_em_dias // 30
idade_em_dias %= 30

# Os dias restantes são os dias
dias = idade_em_dias

# Exibe o resultado no formato anos, meses e dias
print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')