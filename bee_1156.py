s = 1
j = 3
for i in range(1,40):
    s = s + (j) / (2 ** i)
    j += 2
    
print(f'{s:.2f}')