n = int(input("digite um valor para ser o tamanho do array: "))
A = [""] * n
B = [""] * n
for x in range(n):
    A[x]= int(input(f"Digite o {x + 1}ª valor para lista 'A'': "))
for i in range(n):
    B[i] = int(input(f"Digite o {i + 1} valor para lista 'B'': "))
soma = [""] * n
for j in range(n):
    soma[j] = A[j] + B[j]
print(f"o valor da soma dos vetores A e B é igual a: {soma}")