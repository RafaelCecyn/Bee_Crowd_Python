while True:
    n1,n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    if n1 > n2:
        print('Decrescente')
    elif n2 > n1:
        print('Crescente')
    else:
        break