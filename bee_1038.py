codigo, quantidade = input().split(" ")
codigo = int(codigo)
quantidade = int(quantidade)

preco_1 = 4.00
preco_2 = 4.50
preco_3 = 5.00
preco_4 = 2.00
preco_5 = 1.50

if (codigo == 1):
    preco = quantidade * preco_1
    print(f'Total: R$ {preco:.2f}')
elif (codigo == 2):
    preco = quantidade * preco_2
    print(f'Total: R$ {preco:.2f}')
elif (codigo == 3):
    preco = quantidade * preco_3
    print(f'Total: R$ {preco:.2f}')
elif (codigo == 4):
    preco = quantidade * preco_4
    print(f'Total: R$ {preco:.2f}')
elif (codigo == 5):
    preco = quantidade * preco_5
    print(f'Total: R$ {preco:.2f}')