n1 = int(input())
for i in range(n1):
    x,y = input().split()
    x = int(x)
    y = int(y)
    X = min(x,y)
    Y = max(x,y)
    soma = 0
    for j in range(X+1,Y):
        if j % 2 != 0:
            soma += j
    print(soma)