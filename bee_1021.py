nota = float(input())

nota_100 = nota // 100 
resto_100 = nota % 100 
nota_50 = resto_100 // 50 
resto_50 = resto_100 % 50 
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
moeda_050 = resto_1 // 0.5
resto_050 = resto_1 % 0.5
moeda_025 = resto_050 // 0.25
resto_025 = resto_050 % 0.25
moeda_010 = resto_025 // 0.10
resto_010 = resto_025 % 0.10
moeda_005 = resto_010 // 0.05
resto_005 = resto_010 % 0.05
moeda_001 = resto_005 // 0.01



print('NOTAS:')
print(f"{nota_100:.0f} nota(s) de R$ 100.00")
print(f"{nota_50:.0f} nota(s) de R$ 50.00")
print(f"{nota_20:.0f} nota(s) de R$ 20.00")
print(f"{nota_10:.0f} nota(s) de R$ 10.00")
print(f"{nota_5:.0f} nota(s) de R$ 5.00")
print(f"{nota_2:.0f} nota(s) de R$ 2.00")

print('MOEDAS:')
print(f"{nota_1:.0f} moeda(s) de R$ 1.00")
print(f"{moeda_050:.0f} moeda(s) de R$ 0.50")
print(f"{moeda_025:.0f} moeda(s) de R$ 0.25")
print(f"{moeda_010:.0f} moeda(s) de R$ 0.10")
print(f"{moeda_005:.0f} moeda(s) de R$ 0.05")
print(f"{moeda_001:.0f} moeda(s) de R$ 0.01")
