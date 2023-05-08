X = []

for j in range(100):
    X.append(j)



for i in range(100):
    X[i] = float(input())
    if X[i] <= 10:
        print(f'A[{i}] = {X[i]:.1f}')