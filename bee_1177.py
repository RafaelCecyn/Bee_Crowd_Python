v = int(input())

c = 0

for i in range(1000):
    print(f'N[{i}] = {c}')
    c += 1
    if (c==v):
        c=0



