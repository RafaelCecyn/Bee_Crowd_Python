nome_do_func = input()
salario_fixo = float(input())
total_de_vendas = float(input())
comissao = total_de_vendas*0.15
salario_total = salario_fixo + comissao
print(f"TOTAL = R$ {salario_total:.2f}")