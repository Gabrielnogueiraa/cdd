vetores = [0] * 3
maiorv = menorv = 0
soma = 0
pares = []

for x in range(3):
    vetores[x] = int(input(f"digite o {x + 1}º valor: "))
    if x == 0:
        maiorv = menorv = vetores[x]

par = [i for i in vetores if i % 2 == 0]

for i in vetores:
    if i < menorv:
        menorv = i
    if i > maiorv:
        maiorv = i
    soma += i

media = soma / 3
vacm = sum(1 for x in vetores if x > media)

print(f"o maior valor do seu vetor é: {vetores}")
print(f"os pares são: {par}")
print(f"o maior valor do vetor é: {maiorv}")
print(f"o menor valor do vetor é: {menorv}")
print(f"a média dos valores do vetor: {media:.0f}.\n{vacm} são os valores acima da média do vetor.")