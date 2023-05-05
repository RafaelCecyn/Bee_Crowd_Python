inter = 0
gremio = 0
empate = 0
partidas = 0

while True:
    gols_inter,gols_gremio = input().split(" ")
    gols_inter = int(gols_inter)
    gols_gremio = int(gols_gremio)
    
    if gols_inter > gols_gremio:
        inter += 1
    elif gols_gremio > gols_inter:
        gremio += 1
    elif gols_inter == gols_gremio:
        empate += 1
    
    partidas += 1
        
    print("Novo grenal (1-sim 2-nao)")
    novo_grenal= int(input())
    
    if novo_grenal == 2:
        break

print(f'{partidas} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{empate}')

if inter == gremio:
    print("Nao houve vencedor")
elif inter > gremio:
    print("Inter venceu mais")
elif gremio > inter:
    print("Gremio venceu mais")