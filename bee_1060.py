n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

lista = [n1,n2,n3,n4,n5,n6]
contador = 0

for i in lista:
    if i > 0:
        contador +=1

print(f'{contador} valores positivos')

# lista2 = [i for i in lista if i > 0]
# print(lista2)