# Lê o valor de ponto flutuante
valor = float(input())

# Transforma o valor em centavos (para trabalhar com números inteiros)
valor_em_centavos = int(valor * 100)

# Define as notas e moedas disponíveis em centavos
notas_e_moedas = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]

print('NOTAS:')
for nota_moeda in notas_e_moedas[:6]:  # Lida com as notas (100 até 2)
    quantidade = valor_em_centavos // nota_moeda
    valor_em_centavos %= nota_moeda
    print(f'{quantidade} nota(s) de R$ {nota_moeda / 100:.2f}')

print('MOEDAS:')
for nota_moeda in notas_e_moedas[6:]:  # Lida com as moedas (1 até 0.01)
    quantidade = valor_em_centavos // nota_moeda
    valor_em_centavos %= nota_moeda
    print(f'{quantidade} moeda(s) de R$ {nota_moeda / 100:.2f}')