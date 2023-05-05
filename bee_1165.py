N = int(input())
for i in range(N):
    X = int(input())
    divisores = []
    
    for j in range(1,X+1):
        if X % j == 0:
            divisores.append(j)
    if len(divisores) == 2:
        print(f'{X} eh primo')
    else:
        print(f'{X} nao eh primo')