y = [''] * 5
for x in range(0, 5, 1):
    y[x] = int(input(f'Digite seu {x + 1 }ª Número: '))
for j in range(4, -1,-1):
    print(y[j], end=' ')