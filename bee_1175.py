N = [0]*20

for i in range(20):
    N[i] = int(input())

N.reverse()    

for i in range(20):
    print(f'N[{i}] = {N[i]}')