while True:
    n1,n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    if n1 > 0 and n2 > 0:
        print('primeiro')
    elif n1 > 0 and n2 < 0:
        print('quarto')
    elif n1 < 0 and n2 < 0:
        print('terceiro')
    elif n1 < 0 and n2 > 0:
        print('segundo')
    elif n1 == 0 or n2 ==0:
        break
        
        