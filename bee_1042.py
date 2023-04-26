N1,N2,N3 = input().split()
N1 = int(N1)
N2 = int(N2)
N3 = int(N3)

maior = N1

if N2 > maior and N2 > N3:
    maior = N2
elif N3 > N3:
        primeiro_valor = N1
else:
    if N2 > N3:
        primeiro_valor = N1