n1 = int(input())
n2 = int(input())

soma = 0

N1 = min(n1,n2)
N2 = max(n1,n2)

for i in range(N1,N2+1):
    if i % 13 != 0:
        soma += i

print(soma)