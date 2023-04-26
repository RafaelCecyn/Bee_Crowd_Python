salario = float(input())


if salario < 0:
    print("Inválido!")
elif salario <= 400:
    novo_salario = salario * 1.15
    reajuste_ganho = salario * 0.15
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste_ganho:.2f}')
    print("Em percentual: 15 %")
elif salario <= 800:
    novo_salario = salario * 1.12
    reajuste_ganho = salario * 0.12
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste_ganho:.2f}')
    print("Em percentual: 12 %")
elif salario <= 1200:
    novo_salario = salario * 1.10
    reajuste_ganho = salario * 0.10
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste_ganho:.2f}')
    print("Em percentual: 10 %")
elif salario <= 2000:
    novo_salario = salario * 1.07
    reajuste_ganho = salario * 0.07
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste_ganho:.2f}')
    print("Em percentual: 7 %")
elif salario > 2000:
    novo_salario = salario * 1.04
    reajuste_ganho = salario * 0.04
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste_ganho:.2f}')
    print("Em percentual: 4 %")
