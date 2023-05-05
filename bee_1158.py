N = int(input())

for i in range(N):
    X,Y = input().split(' ')
    X = int(X)
    Y = int(Y)
    soma = []

    if X % 2 == 0:
        for i in range(X+1,X+(Y*2),2):
            soma.append(i)
        print(sum(soma))
    else:
        for i in range(X,X+ (Y*2)-1,2):
            soma.append(i)
        print(sum(soma))