tempo = int(input())
velocidade_media = int(input())

distancia = tempo * velocidade_media

autonomia = 12

litros = distancia / autonomia

print(f'{litros:.3f}')