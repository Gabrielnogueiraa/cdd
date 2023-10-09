q = [''] * 10
for y in range(10):
    q[y] = int(input(f'Digite o {y + 1}ª Número: '))
x = int(input('Digite o valor que vai multiplicar cada elemento da lista: '))
m = [''] * 10
for i in range(10):
    m[i] = q[i] * x
print(f'os valores colocados na lista: {q}\nlista multiplicada por {x}: {m}')