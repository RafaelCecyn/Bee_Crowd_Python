n1,n2 = input().split()
n1 = int(n1)
n2 = int(n2)

if n1 < n2:
    tempo = n2 - n1
else:
    tempo = (24 - n1) + n2
    
print(f'O JOGO DUROU {tempo} HORA(S)')