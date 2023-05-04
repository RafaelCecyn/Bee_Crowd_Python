# n1,n2 = input().split(' ')
# n1 = int(n1)
# n2 = int(n2)
# j = 1
# for i in range(n1-2,n2+1,1):
#     print(j, j+1, j+2)
#     print()
#     j += 3

l, n = [int(x) for x in input().split()]
for i in range(1, n+1):
    print(i, end='')
    if i % l != 0: print(end=' ')
    else: print()
