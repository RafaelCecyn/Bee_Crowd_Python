n1 = int(input())
dentro = 0
fora = 0

for i in range(n1):
    x = int(input())
    
    if x >=10 and  x <= 20:
        dentro += 1
    else:
        fora += 1
        
print(f'{dentro} in')    
print(f'{fora} out')    
