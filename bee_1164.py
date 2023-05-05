N = int(input())
for i in range(N):
    X = int(input())
    divisores = []
    
    for j in range(1,X):
        if X % j == 0:
            divisores.append(j)
    if sum(divisores) == X:
        print(f'{X} eh perfeito')
    else:
        print(f'{X} nao eh perfeito')