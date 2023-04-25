idade = int(input())

idade_em_anos = idade // 365
resto_em_anos = idade % 365
idade_em_mes = resto_em_anos // 30
resto_em_mes = resto_em_anos % 30
dias = resto_em_mes

print(f'{idade_em_anos} ano(s)')
print(f'{idade_em_mes} mes(es)')
print(f'{dias} dia(s)')