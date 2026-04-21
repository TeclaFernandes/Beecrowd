while True:
    try:
        # Lê o valor de A
        A = int(input())
        
        # Verifica se A é divisível por 6
        if A % 6 == 0:
            print("Y")
        else:
            print("N")
    except EOFError:
        break
