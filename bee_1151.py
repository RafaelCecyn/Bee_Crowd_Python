N = int(input())

sequencia = [0,1]
result = 0

for i in range(N-2):
    result = sequencia[-1] + sequencia[-2]
    sequencia.append(result)

print(' '.join(map(str,sequencia)))

    