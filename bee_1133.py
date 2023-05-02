n1 = int(input())
n2 = int(input())

N1 = min(n1,n2)
N2 = max(n1,n2)

for i in range(N1+1,N2):
    if i % 5 == 2 or i % 5 ==3:
        print(i)