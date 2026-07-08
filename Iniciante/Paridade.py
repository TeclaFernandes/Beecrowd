while True:
    try:
        s = input()

        quantidade = s.count('1')

        if quantidade % 2 == 0:
            print(s + "0")
        else:
            print(s + "1")

    except EOFError:
        break