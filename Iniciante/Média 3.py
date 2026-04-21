N1, N2, N3, N4 = map(float, input().split())

media = (N1*2 + N2*3 + N3*4 + N4*1)/(10)
print(f'Media: {media:.1f}')
if media >= 7:
    print(f'Aluno aprovado.')
elif media < 5:
    print(f'Aluno reprovado.')
else: 
    print(f'Aluno em exame.')
    nota_exame = float(input())
    print(f'Nota do exame: {nota_exame}')
    media_final  = (media + nota_exame)/2
    if media_final >= 5:
        print(f'Aluno aprovado.')
    else:
        print(f'Aluno reprovado.')
    print(f'Media final: {media_final}')