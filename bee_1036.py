# Fórmula de Bhaskara
A,B,C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)
delta = ((B**2) - 4 * A * C)

if (delta < 0) or (A == 0):
    print("Impossivel calcular")
elif (delta > 0):
    R1 = ((-B) + (delta**0.5)) / (2 * A)
    R2 = ((-B) - (delta**0.5)) / (2 * A)
    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')