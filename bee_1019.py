tempo = int(input())

valor_em_hora = tempo // 3600
resto_em_hora = tempo % 3600
valor_em_minutos = resto_em_hora // 60
resto_em_minutos = resto_em_hora % 60
segundos = resto_em_minutos

print(f'{valor_em_hora}:{valor_em_minutos}:{segundos}') 
 
 
