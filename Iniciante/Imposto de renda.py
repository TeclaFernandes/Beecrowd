salario = float(input())

imposto = 0.0

if salario <= 2000.00:
    print("Isento")
else:
    if salario > 2000.00:
        base = min(salario, 3000.00) - 2000.00
        imposto += base * 0.08

    if salario > 3000.00:
        base = min(salario, 4500.00) - 3000.00
        imposto += base * 0.18

    if salario > 4500.00:
        base = salario - 4500.00
        imposto += base * 0.28

    print(f"R$ {imposto:.2f}")