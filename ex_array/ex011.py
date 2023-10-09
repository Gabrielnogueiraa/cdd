v = [""] * 30
for i in range(5):
    v[i] = int(input(f"digite o {i + 1}ª número: "))
c = 0
n = int(input("escreva um numero para saber quantas vezes ele aparece no vetor: "))
for j in v:
    if j == n:
        c += 1
print(f"o numero {n} apareceu {c} vezes no vetor.")