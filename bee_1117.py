notas_validas = []
while True:
    nota = float(input())
    
    if nota < 0 or nota >10:
        print('nota invalida')
        
    else:
        notas_validas.append(nota)
    
    if len(notas_validas) == 2:
        media = sum(notas_validas) / len(notas_validas)
        print(f'media = {media:.2f}')
        break
        

