N1,N2,N3,N4 = input().split(" ")
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)



media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

print(f'Media: {media:.1f}')

if media < 5.0:
    print("Aluno reprovado.")
elif media >= 5.0 and media <= 6.9:
    print("Aluno em exame.")
    nota_final = float(input().split()[0])
    print(f'Nota do exame: {nota_final:.1f}')
    media_final = (media + nota_final) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {media_final:.1f}")
    else:
        print("Aluno reprovado")
    
elif media > 7.0:
    print("Aluno aprovado.")