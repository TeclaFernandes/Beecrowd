# Lê os dados da peça 1
codigo_peca1, quantidade_peca1, valor_unitario_peca1 = input().split()
codigo_peca1 = int(codigo_peca1)
quantidade_peca1 = int(quantidade_peca1)
valor_unitario_peca1 = float(valor_unitario_peca1)

# Lê os dados da peça 2
codigo_peca2, quantidade_peca2, valor_unitario_peca2 = input().split()
codigo_peca2 = int(codigo_peca2)
quantidade_peca2 = int(quantidade_peca2)
valor_unitario_peca2 = float(valor_unitario_peca2)

# Calcula o valor total a ser pago
valor_total = (quantidade_peca1 * valor_unitario_peca1) + (quantidade_peca2 * valor_unitario_peca2)

# Imprime o resultado formatado
print("VALOR A PAGAR: R$ {:.2f}".format(valor_total))