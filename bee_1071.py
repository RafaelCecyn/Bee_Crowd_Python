n1 = int(input())
n2 = int(input())

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
    
soma_impar = 0
    
for i in range(menor+1,maior):
    if i % 2 != 0:
        soma_impar += i

print(soma_impar)
    
