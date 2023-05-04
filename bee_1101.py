while True:
    n1,n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    
    N1 = min(n1,n2)
    N2 = max(n1,n2)
    
    if N1 <= 0 or N2 <= 0:
        break
    soma = 0
    for i in range(N1,N2+1):
        soma += i
        print(i,sep=' ',end=' ')
      
    print(f'Sum={soma}')
    