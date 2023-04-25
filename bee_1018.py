nota = int(input())
print(nota)

nota_100 = nota // 100 # 5
resto_100 = nota % 100 # 76
nota_50 = resto_100 // 50 # 1
resto_50 = resto_100 % 50 # 26
nota_20 = resto_50 // 20
resto_20 = resto_50 % 20
nota_10 = resto_20 // 10
resto_10 = resto_20 % 10
nota_5 = resto_10 // 5
resto_5 = resto_10 % 5
nota_2 = resto_5 // 2
resto_2 = resto_5 % 2
nota_1 = resto_2 // 1
resto_1 = resto_2 % 1

print(f"{nota_100} nota(s) de R$ 100,00")
print(f"{nota_50} nota(s) de R$ 50,00")
print(f"{nota_20} nota(s) de R$ 20,00")
print(f"{nota_10} nota(s) de R$ 10,00")
print(f"{nota_5} nota(s) de R$ 5,00")
print(f"{nota_2} nota(s) de R$ 2,00")
print(f"{nota_1} nota(s) de R$ 1,00")
