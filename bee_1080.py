maior = -9999999
for i in range(100):
    numero = int(input())
    if numero > maior:
        maior = numero
        pos = i
print(maior)
print(pos+1)