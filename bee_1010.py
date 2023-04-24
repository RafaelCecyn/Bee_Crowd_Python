linha1 = input().split()
cod_peca_1 = int(linha1[0])
quantidade_1 = int(linha1[1])
valor_1 = float(linha1[2])
preco_1 = quantidade_1*valor_1

linha2 = input().split()
cod_peca_2 = int(linha2[0])
quantidade_2 = int(linha2[1])
valor_2 = float(linha2[2])
preco_2 = quantidade_2*valor_2

valor_total = preco_1 + preco_2

print(f"VALOR A PAGAR: R$ {valor_total:.2f}")

# linha = input().split()
# print(linha)