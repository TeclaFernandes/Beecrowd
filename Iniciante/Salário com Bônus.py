#Nome do vendedor
nome = input()

#Salário fixo
salario = float(input())

#Total da venda efetuadas no mês (em dinheiro)
vendas = float(input())

#Comissã de 15% sobre cada venda feita
#comissa = (vendas/100)*15
#Calculando...
salario_final = salario + (vendas/100*15)

#Total a receber no final do mês
print('TOTAL = R$ {:.2f}'.format(salario_final))