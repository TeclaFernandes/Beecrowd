#Número do funcionário
NF = int(input())

#Número de horas trabalhadas
HT = float(input())

#Valor a receber por hora trabahadas
VH = float(input())

#Calculando...
SALARIO = HT * VH

#Salário a receber
print('NUMBER =', NF)
print('SALARY = U$ {:.2f}'.format(SALARIO))