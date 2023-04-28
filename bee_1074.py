n1 = int(input())

for i in range(n1):
    i = int(input())
    if i %2 == 0 and i > 0 :
        print('EVEN POSITIVE')
    elif i %2 == 0 and i < 0 :
        print('EVEN NEGATIVE')
    elif i %2 != 0 and i < 0 :
        print('ODD NEGATIVE')
    elif i %2 != 0 and i > 0 :
        print('ODD POSITIVE')
    elif i == 0:
        print('NULL')
        