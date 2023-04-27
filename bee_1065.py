n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

lista = [n1,n2,n3,n4,n5]
contador = 0

for i in lista:
    if i %2 == 0:
        contador +=1

print(f'{contador} valores pares')