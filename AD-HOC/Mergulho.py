import numpy as np

while True:
    try:
        
        E, S = map(int, input().split())
        vetor_retorno = np.array(input().split(), dtype=int)
        vetor_id = np.zeros(E+1, dtype=int)
        
        if E == S:
            print('*')
            continue
        
        for i in vetor_retorno:
            vetor_id[i] = 1
            
        for val in range(1, len(vetor_id)):
            if vetor_id[val] == 0:
                print(val, end=' ')
            
        print('')
        
    except EOFError:
        break