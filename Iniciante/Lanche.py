# CÓDIGO   -   ESPECIFICAÇÃO   -   PREÇO
#    1     -  Cachorro Quente  -  R$ 4,00
#    2     -  X-Salada         -  R$ 4,50
#    3     -  X-Bacon          -  R$ 5,00
#    4     -  Torrada Simples  -  R$ 2,00
#    5     -  Refrigerante     -  R$ 1,50

codigo_produto = int(input())
quantidade_produto = int(input())

if codigo_produto == 1:
    preco_final = 4 * quantidade_produto
elif codigo_produto == 2:
    preco_final = 4.5 * quantidade_produto
elif codigo_produto == 3:
    preco_final = 5 * quantidade_produto
elif codigo_produto == 4:
    preco_final = 2 * quantidade_produto
elif codigo_produto == 5:
    preco_final = 1.5 * quantidade_produto
else: 
    print('Código inválido... Tente novamente inserir a informação.')

print(f'Total: R$ {preco_final:.2f}')