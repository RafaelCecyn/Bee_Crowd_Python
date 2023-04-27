n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

lista = [n1,n2,n3,n4,n5]
contador_par = 0
contador_impar = 0
contador_positivo = 0
contador_negativo = 0

for i in lista:
    if i %2 == 0:
        contador_par +=1

for i in lista:
    if i %2 != 0:
        contador_impar +=1

for i in lista:
    if i > 0:
        contador_positivo +=1

for i in lista:
    if i < 0:
        contador_negativo +=1



print(f'{contador_par} valor(es) par(es)')
print(f'{contador_impar} valor(es) impar(es)')
print(f'{contador_positivo} valor(es) positivo(s)')
print(f'{contador_negativo} valor(es) negativo(s)')