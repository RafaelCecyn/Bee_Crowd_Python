n1 = int(input())

for i in range(n1):
    x,y = input().split()
    x = float(x)
    y = float(y)
    
    if y == 0:
        print('divisao impossivel')
    else:
        divisao = x / y 
        print(f'{divisao:.1f}')
    
    
    
