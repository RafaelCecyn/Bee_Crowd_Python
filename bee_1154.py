soma_de_dados = []

while True:
    numero = int(input())
    
    if numero < 0:
        break
    else:
        soma_de_dados.append(numero)

media = sum(soma_de_dados) / len(soma_de_dados)
print(f'{media:.2f}')