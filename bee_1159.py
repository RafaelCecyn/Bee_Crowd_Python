while True:
    soma = []
    X = int(input())
    
    if X == 0:
        break
    else: 
        if X % 2 == 0:
            for i in range(X,X+ (5*2),2):
                soma.append(i)
            print(sum(soma))
        else:
            for i in range(X+1,X+ (5*2),2):
                 soma.append(i)
            print(sum(soma))
            